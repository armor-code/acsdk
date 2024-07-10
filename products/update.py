import asyncio
from itertools import chain
from .get import get_product_by_id
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

async def update_product_by_id(session, product_id, partial_product_payload):
    product_payload = await get_product_by_id(session, product_id)

    partial_product_payload["id"] = product_id

    # FIXME: Replace this shallow merge with a deep merge.
    response = await fetch(session, "put", "/user/product/", json={**product_payload, **partial_product_payload})

    return response.ok
