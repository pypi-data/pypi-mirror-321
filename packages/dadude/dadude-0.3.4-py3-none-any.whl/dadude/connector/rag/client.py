import os
from dotenv import load_dotenv
import httpx

load_dotenv()


def rag_zeus_demo(query: str):
    url = os.getenv("RAG_URL", "http://192.168.18.214:5047/api/predict")

    payload = {"data": [query]}
    headers = {"content-type": "application/json"}

    response = httpx.post(url, json=payload, headers=headers)

    print(response.json())


if __name__ == "__main__":
    rag_zeus_demo("Howdy!")
