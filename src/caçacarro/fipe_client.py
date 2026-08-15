import os

import httpx
from dotenv import load_dotenv
from connect_db import insert_marcas 
load_dotenv()

FIPE_BASE_URL = "https://fipe.parallelum.com.br/api/v2"


def _headers() -> dict[str, str]:
    token = os.environ["FIPE_API_TOKEN"]
    return {"X-Subscription-Token": token}


def get_references() -> list[dict]:
    resp = httpx.get(f"{FIPE_BASE_URL}/cars/brands", headers=_headers())
    resp.raise_for_status()
    return resp.json()



if __name__ == "__main__":
    for ref in get_references():
        insert_marcas(ref["name"])
