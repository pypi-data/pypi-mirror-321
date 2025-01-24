from itertools import chain, islice
from functools import partial
import os
import base64
import gzip
import io
import json
from msgspec import Struct
import msgspec.json as msg_json
from tqdm import tqdm
import httpx
from fire import Fire

from dadude.connector.tidb.source import TidbTable


class PatentSectionText(Struct):
    patent_id: str
    lang: str
    is_translation: bool = False
    title: str = ""
    abstract: str = ""
    claim: str = ""
    description: str = ""

    def load_section_text(self, section, text):
        match section:
            case "title":
                self.title = text
            case "abstract":
                self.abstract = text
            case "claim":
                self.claim = text
            case "description":
                self.description = text
            case _:
                raise KeyError(f"Invalid section: {section}")


os.environ["DAAS_URL"] = os.getenv(
    "DAAS_URL",
    "http://stage-s-dw-data-api-internet.patsnap.info/dw-data-api/daas/sql/select",
)
os.environ["X_PATSNAP_FROM"] = os.getenv(
    "X_PATSNAP_FROM", "s-patsnaprd-dadude-tidb-client"
)


def chunks(iterable, size):
    iterator = iter(iterable)
    for first in iterator:
        yield list(chain([first], islice(iterator, size - 1)))


def decompress_tidb(byte_stream):
    decoded_data = base64.b64decode(byte_stream)
    zipfile = gzip.GzipFile(fileobj=io.BytesIO(decoded_data))
    text = zipfile.read().decode("utf8")
    return text


def batch_get_from_table(table, patent_ids, lang):
    headers = {
        "X-PATSNAP-FROM": os.getenv("X_PATSNAP_FROM", ""),
    }
    daas_url = os.getenv(
        "DAAS_URL",
        "http://stage-s-dw-data-api-internet.patsnap.info/dw-data-api/daas/sql/select",
    )
    query = f"select `patent_id`, `content` from {table.table_name} where patent_id in (':patent_id') and lang = ':lang'"
    body = {
        "sql": query,
        "params": {
            "patent_id": patent_ids,
            "lang": lang,
        },
    }
    batch_response_items = httpx.post(daas_url, json=body, headers=headers)
    all_ret = batch_response_items.json().get("data", []).get("results", [])
    res = []
    for ret in all_ret:
        res.append(
            {
                "patent_id": ret.get("patent_id"),
                "content": decompress_tidb(ret.get("content", "")),
            }
        )
    return res


class Database:
    def __init__(self):
        self.patent = TidbTable("ads_patent")
        self.patent_title = TidbTable("dws_patent_title")
        self.patent_abstract = TidbTable("dws_patent_abstract")
        self.patent_claim = TidbTable("dws_patent_claim_v2")
        self.patent_description = TidbTable("dws_patent_description")
        self.patent_trans_title = TidbTable("dws_patent_translation_title")
        self.patent_trans_abstract = TidbTable("dws_patent_translation_abstract")
        self.patent_trans_claim = TidbTable("dws_patent_translation_claim")
        self.patent_trans_description = TidbTable("dws_patent_translation_description")
        self.valid_sections = ["title", "abstract", "claim", "description"]
        self.original_table_map = {
            "title": self.patent_title,
            "abstract": self.patent_abstract,
            "claim": self.patent_claim,
            "description": self.patent_description,
        }
        self.translation_table_map = {
            "title": self.patent_trans_title,
            "abstract": self.patent_trans_abstract,
            "claim": self.patent_trans_claim,
            "description": self.patent_trans_description,
        }

    def get_text_by_patent_id_section_lang_trans(
        self, patent_id, section, lang, use_trans=False
    ):
        assert section in self.valid_sections
        lang = lang.upper()
        table = (
            self.translation_table_map[section]
            if use_trans
            else self.original_table_map[section]
        )
        items = table.query(
            "patent_id",
            patent_id,
            return_dict=True,
            attributes_to_get=["patent_id", "content", "lang"],
            filter_condition=[{"key": "lang", "value": lang, "op": "="}],
        )
        if len(items) > 0:
            return decompress_tidb(items[0].get("content", ""))  # type: ignore
        return ""

    def batch_get_text_by_patent_id_section_lang_trans(
        self, patent_ids, section, lang, use_trans=False
    ):
        assert section in self.valid_sections
        lang = lang.upper()
        table = (
            self.translation_table_map[section]
            if use_trans
            else self.original_table_map[section]
        )
        batch_get_items = batch_get_from_table(table, patent_ids, lang)
        return batch_get_items


def process_mat_pids(
    db,
    input_path,
    output_path,
    section,
    target_country: list[str] = [],
    target_lang="CN",
    batch_size=1000,
):
    # load msgspec encoder
    enc = msg_json.Encoder()

    to_trans_cnt_list = [cnt for cnt in target_country if cnt != target_lang]
    original_patent_ids = []
    translation_patent_ids = []
    with open(input_path, "r") as f:
        reader = []
        for line in f:
            reader.append(json.loads(line))
        for row in tqdm(reader):
            if len(target_country) == 0 or target_country is None:
                original_patent_ids.append(row["patent_id"])
            else:
                if row["country"] not in target_country:
                    continue
                if row["country"] == target_lang:
                    original_patent_ids.append(row["patent_id"])
                if row["country"] in to_trans_cnt_list:
                    translation_patent_ids.append(row["patent_id"])

    total_ori = len(original_patent_ids)
    total_trans = len(translation_patent_ids)
    print(f"Original patent ids: {total_ori}")
    print(f"Translation patent ids: {total_trans}")

    with open(output_path, "wt") as g:
        print(f"Start getting the {section} text for original patent ids")
        for batch in tqdm(
            chunks(original_patent_ids, batch_size), total=total_ori // batch_size
        ):
            ori_text_list = db.batch_get_text_by_patent_id_section_lang_trans(
                batch,
                section,
                target_lang,
                use_trans=False,
            )
            for item in ori_text_list:
                input_obj = PatentSectionText(
                    patent_id=item["patent_id"],
                    lang=target_lang,
                    is_translation=False,
                )
                input_obj.load_section_text(section, item["content"])
                g.write(enc.encode(input_obj).decode("utf-8") + "\n")

        print(f"Start getting the {section} text for translation patent ids")
        for batch in tqdm(
            chunks(translation_patent_ids, batch_size), total=total_trans // batch_size
        ):
            tran_text_list = db.batch_get_text_by_patent_id_section_lang_trans(
                batch,
                section,
                target_lang,
                use_trans=True,
            )
            for item in tran_text_list:
                input_obj = PatentSectionText(
                    patent_id=item["patent_id"],
                    lang=target_lang,
                    is_translation=True,
                )
                input_obj.load_section_text(section, item["content"])
                g.write(enc.encode(input_obj).decode("utf-8") + "\n")


if __name__ == "__main__":
    db = Database()

    # single query
    # patent_id = "cdd8f73e-f3d7-4fb6-bd17-fb9efcd27182"
    # section = "title"
    # lang = "en"
    # text = db.get_text_by_patent_id_section_lang_trans(patent_id, section, lang, use_trans=True)
    # print(text)

    ## batch query
    # patent_ids = [
    #     "1e796769-8304-4191-ac10-a260d3e3bc52",
    #     "1e93712e-6463-4640-b611-be568109c7f1",
    # ]
    # text_list = db.batch_get_text_by_patent_id_section_lang_trans(patent_ids, section, lang)
    # print(text_list)

    # mat_pid_path = "/home/kevinxu/data/silver/searchapi_substance_sample_pids_248k.json"
    # mat_title_path = (
    #     "/home/kevinxu/data/gold/searchapi_substance_sample_pids_desc_248k.json"
    # )
    # process_mat_pids(
    #     db,
    #     mat_pid_path,
    #     mat_title_path,
    #     # "abstract",
    #     "description",
    #     target_lang="EN",
    #     # ["CN", "KR", "JP", "TW", "HK"],
    #     batch_size=100,
    # )
    process_mat_pids_db = partial(process_mat_pids, db=db)
    Fire(process_mat_pids_db)
