from msgspec import Struct, field
import httpx
from tenacity import retry, stop_after_attempt
from loguru import logger


class SearchApiSubstancePatentQuery(Struct):
    substance_id: str
    substance_names: list[str] = field(default_factory=list)
    rows: int = 100
    fields: list[str] = field(default_factory=list)

    @classmethod
    def default(cls):
        return cls(
            substance_id="aa473360-4b4b-4db1-b2ce-e4922afd3152",
            substance_names=[],
            rows=100,
            fields=["_id"],
        )


class SearchApiSubstancePatentResponse(Struct):
    params: dict
    num_found: int
    top_docs: list[dict]


@retry(stop=stop_after_attempt(3))
def search_patent_by_substance_id(
    query: SearchApiSubstancePatentQuery,
) -> SearchApiSubstancePatentResponse | None:
    url = "https://stage-s-search-patent-solr-internet.patsnap.info/patsnap/PATENT_20241018/select"

    alias_name_str = " OR ".join([f'"{n}"' for n in query.substance_names])
    full_query = f"SUBSTANCE_IDS:{query.substance_id}^3 OR TACD: ({alias_name_str})"
    logger.debug(f"Full query: {full_query}")
    querystring = {
        "q": full_query,
        "rows": str(query.rows),
        "fl": query.fields,
    }

    response = httpx.get(url, params=querystring)

    try:
        req = response.json()
        response = SearchApiSubstancePatentResponse(
            params=req["responseHeader"]["params"],
            num_found=req["response"]["numFound"],
            top_docs=req["response"]["docs"],
        )
        return response
    except Exception as e:
        logger.error(f"Error in search_patent_by_substance_id: {e}")
        return None


if __name__ == "__main__":
    print(search_patent_by_substance_id(SearchApiSubstancePatentQuery.default()))
