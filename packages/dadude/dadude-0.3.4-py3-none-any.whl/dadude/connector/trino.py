import os

import httpx
from dotenv import load_dotenv


load_dotenv()


def trino_login():
    user_email = os.getenv("PATSNAP_USER_EMAIL", "")
    password = os.getenv("PATSNAP_PASSWORD", "")
    url = "http://s-gateway-dataprod-tencent.patsnap.info/s-dw-data-analysis-api/api/auth/login"

    payload = {"username": user_email, "password": password}
    headers = {"Content-Type": "application/json", "content-type": "application/json"}

    response = httpx.post(url, json=payload, headers=headers)

    ret = response.json()
    return ret["token"]


def export_query(token: str, query: str):
    url = "http://s-gateway-dataprod-tencent.patsnap.info/s-dw-data-analysis-api/api/analysis/export"

    payload = {
        "athenaAccount": "tx_us",
        "database": "tmp",
        "sql": query,
        "isSync": True,
        "isExport": True,
    }
    headers = {
        "from": "X-xuzhangda-dadude",
        "X-Authorization": token,
        "Content-Type": "application/json",
    }

    response = httpx.post(url, json=payload, headers=headers, timeout=600)

    return response.json()


if __name__ == "__main__":
    # query = "select * from pd_dw.dws_material_substance_entity_v2 where source in ('3', '2', '2,3')"
    query = "select * from pd_dw.dws_material_property_entity_v3"
    token = trino_login()
    print(export_query(token, query))
    # TODO: implement:
    # s3 download
    # duckdb convert to json
    # save to local cache
