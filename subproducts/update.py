import asyncio
from itertools import chain
from .get import get_subproduct_by_id
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

async def update_subproduct_by_id(session, subproduct_id, partial_subproduct_payload):
    subproduct_payload = await get_subproduct_by_id(session, subproduct_id)

    partial_subproduct_payload["id"] = subproduct_id

    # FIXME: Replace this shallow merge with a deep merge.
    response = await fetch(session, "put", "/api/sub-product", json={**subproduct_payload, **partial_subproduct_payload})

    return response.ok
