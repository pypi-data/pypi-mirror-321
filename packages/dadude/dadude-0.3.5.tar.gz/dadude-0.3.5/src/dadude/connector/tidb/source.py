import httpx
from httpx import Response
import os
from dataclasses import dataclass
from typing import Optional, Union, List


@dataclass
class DaasApiParams:
    entity_id: Union[str, List[str]]
    attributes_to_get: str
    page_size: int = 10000
    index: Optional[str] = None
    filter_condition: Optional[List[dict]] = None


@dataclass
class DaasApiRequestBody:
    sql: str
    params: dict

    def json(self):
        return {"sql": self.sql, "params": self.params}


@dataclass
class MetaDaasApiResponse:
    response_body: Response
    fields: Optional[list] = None
    primary_key: Optional[str] = None
    index_list: Optional[list] = None

    def __post_init__(self):
        if self.response_body.status_code != 200:
            error_msg = f"Meta daas api request error: {self.response_body.status_code} {self.response_body.text}"
            raise Exception(error_msg)

        meta_info = self.response_body.json()
        if not meta_info["status"] or "data" not in meta_info:
            error_msg = (
                f"error_msg: {meta_info['error_msg']}\n"
                f"Req URL: {self.response_body.url}"
            )
            raise Exception(error_msg)
        meta_info = meta_info["data"]
        # if meta_info['database_info']['db_type'] not in ['tidb', 'rest']:
        #     raise Exception(f"{meta_info['table_name']} is not a tidb/rest table")
        self.fields = [f["field_name"] for f in meta_info["fields"]]
        index_infos = meta_info["index_infos"]
        index_list = []
        primary_key = None
        for idx in index_infos:
            if idx["index_name"].startswith("idx_"):
                index_list.extend(idx["keys"])
            if idx["index_name"] == "PRIMARY":
                if len(idx["keys"]) == 1:
                    primary_key = idx["keys"][0]
        self.primary_key = primary_key
        self.index_list = index_list


@dataclass
class DaasApiResponse:
    response_body: Response
    items: Optional[list] = None
    last_cursor: Optional[int] = None

    def __post_init__(self):
        if self.response_body.status_code != 200:
            error_msg = f"daas api request error: {self.response_body.status_code} {self.response_body.text}"
            raise Exception(error_msg)
        res = self.response_body.json()
        if not res["status"] or "data" not in res:
            raise Exception(res["error_msg"])
        self.items = res["data"].get("results", [])
        self.last_cursor = res["data"].get("last_cursor")


class DaasApiClient:
    def __init__(self, table_name, daas_url):
        self.table_name = table_name
        self.daas_url = daas_url
        self.schema = self.query_meta_table()

    def get_schema(self):
        return self.schema

    def query_table(self, params: DaasApiParams):
        query = self.build_query(params)
        items = []
        response = self.send_request(query)
        if response.items:
            items.extend(response.items)
        while response.last_cursor:
            query = self.build_query(params, last_cursor=response.last_cursor)
            response = self.send_request(query)
            if response.items:
                items.extend(response.items)
        return items

    def query_meta_table(self) -> MetaDaasApiResponse:
        url = self.daas_url
        url = (
            url.rstrip("daas/sql/select") + f"/metadata/table/{self.table_name}/detail"
        )
        from_head = (
            os.getenv("X_PATSNAP_FROM") or os.getenv("SERVICE-NAME") or "s-s-s-s"
        )
        header = {"X-PatSnap-From": from_head}
        ret = httpx.get(url, headers=header)
        return MetaDaasApiResponse(ret)

    def build_query(
        self, query_params: DaasApiParams, last_cursor=None, page_size=10000
    ) -> DaasApiRequestBody:
        if query_params.index:
            query_key = query_params.index
        else:
            query_key = self.schema.primary_key
        params = {query_key: query_params.entity_id}
        filter_str = ""
        if query_params.filter_condition:
            for item in query_params.filter_condition:
                key, value = item["key"], item["value"]
                op = item.get("op", "=")
                if op == "in":
                    key_tmpl = f"(':{key}')"
                else:
                    key_tmpl = f"':{key}'"
                filter_str += f" and {key} {op} {key_tmpl}"
                params[key] = value

        if last_cursor:
            consistent_read_sql = f"limit {last_cursor}, {page_size}"
        else:
            consistent_read_sql = ""
        if not isinstance(query_params.entity_id, list):
            sql = f"select {query_params.attributes_to_get} from {self.table_name} where {query_key} = ':{query_key}' {filter_str} {consistent_read_sql}"
        else:
            sql = f"select {query_params.attributes_to_get} from {self.table_name} where {query_key} in (':{query_key}') {filter_str} {consistent_read_sql}"
        data = {"sql": sql, "params": params}
        return DaasApiRequestBody(**data)

    def send_request(self, request_body: DaasApiRequestBody) -> DaasApiResponse:
        daas_url = self.daas_url
        from_head = (
            os.getenv("X_PATSNAP_FROM") or os.getenv("SERVICE-NAME") or "s-s-s-s"
        )
        headers = {"X-PatSnap-From": from_head, "Content-Type": "application/json"}
        res = httpx.post(url=daas_url, headers=headers, json=request_body.json())
        return DaasApiResponse(res)


class DoesNotExist(Exception):
    def __init__(
        self, message="Item does not exist in tidb", table_name=None, hash_key=None
    ):
        self.message = message
        if table_name:
            self.message += f" {table_name}"
        if hash_key:
            self.message += f": {hash_key}"
        super().__init__(self.message)


class MetaData:
    def __init__(self, data_dict, hash_key_name, schema, _range_keyname=None):
        self.attribute_values = data_dict
        self._hash_keyname = hash_key_name
        self._range_keyname = _range_keyname
        for key in schema:
            setattr(self, key, None)
        for key, value in data_dict.items():
            setattr(self, key, value)

    def __iter__(self):
        return (item for item in self.__dict__.items())


class MetaTable:
    def __init__(self, table_name):
        self.table_name = table_name


class TidbTable:
    def __init__(self, table_name, daas_url=None):
        self.table_name = table_name
        if not daas_url:
            daas_url = os.getenv(
                "DAAS_URL",
                "http://s-dw-data-api-release.patsnap.info/dw-data-api/daas/sql/select",
            )
        self.daas_client = DaasApiClient(table_name, daas_url)
        self.schema = self.daas_client.schema
        self.Meta = MetaTable(table_name)

    def get(self, hash_key, attributes_to_get=None, **kwargs):
        if not self.schema.primary_key:
            raise Exception("table has no hash_key")
        attributes_to_get = self._build_query_field(attributes_to_get)
        page_size = kwargs.get("page_size", 10000)
        ret = self.daas_client.query_table(
            DaasApiParams(
                entity_id=hash_key,
                page_size=page_size,
                attributes_to_get=attributes_to_get,
            )
        )
        if ret:
            if kwargs.get("return_dict"):
                return ret[0]
            return MetaData(ret[0], self.schema.primary_key, self.schema.fields)
        raise DoesNotExist(hash_key=hash_key)

    def batch_get(self, hash_keys, attributes_to_get=None, return_dict=False, **kwargs):
        if not hash_keys:
            return []
        attributes_to_get = self._build_query_field(attributes_to_get)
        page_size = kwargs.get("page_size", 10000)
        ret = self.daas_client.query_table(
            DaasApiParams(
                entity_id=hash_keys,
                page_size=page_size,
                attributes_to_get=attributes_to_get,
            )
        )

        if kwargs.get("resort", False) and self.schema.primary_key:
            sort_dict = {}
            for item in ret:
                sort_dict[item[self.schema.primary_key]] = item
            sorted_ret = []
            for key in hash_keys:
                if key in sorted_ret:
                    sorted_ret.append(sort_dict[key])
            ret = sorted_ret

        if return_dict:
            return ret
        else:
            all_items = [
                MetaData(item, self.schema.primary_key, self.schema.fields)
                for item in ret
            ]
        return all_items

    def query(
        self,
        key,
        value,
        attributes_to_get=None,
        return_dict=False,
        filter_condition=None,
        **kwargs,
    ):
        """
        :param key: table index name, -> string
        :param value: -> list of list of string
        :param attributes_to_get:
        :param return_dict: if True, return dictionary, else object.
        :param filter_condition: return items satisfy the condition, -> list of dict
                                 eg: [{"key": "data_status", "value": "ACTIVE", "op": "="}]
                                 "key" and "value" are required,
                                 "op" is optional, default: "=".
        :return:
        """
        if not value:
            return []
        attributes_to_get = self._build_query_field(attributes_to_get)
        page_size = kwargs.get("page_size", 10000)
        ret = self.daas_client.query_table(
            DaasApiParams(
                entity_id=value,
                attributes_to_get=attributes_to_get,
                filter_condition=filter_condition,
                index=key,
                page_size=page_size,
            )
        )
        if return_dict:
            return ret
        else:
            all_items = [
                MetaData(item, self.schema.primary_key, self.schema.fields)
                for item in ret
            ]
        return all_items

    def _build_query_field(self, attributes_to_get):
        if not attributes_to_get and self.schema.fields:
            attributes_to_get = ", ".join(self.schema.fields)
        elif not attributes_to_get:
            return ""
        else:
            for _field in attributes_to_get:
                if _field not in self.schema.fields:
                    raise Exception(f"`{self.table_name}` has no key `{_field}`")
            attributes_to_get = ", ".join(attributes_to_get)

        return attributes_to_get

    def __str__(self):
        return self.table_name
