import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

async def delete_subproduct_by_id(session, subproduct_id):
    response = await fetch(session, "delete", "/api/sub-product/" + str(subproduct_id))

    return response.ok
