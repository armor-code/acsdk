import asyncio
from itertools import chain

from ..util import fetch, Promise

async def delete_product_by_id(session, product_id):
    response = await fetch(session, "delete", "/user/product/" + str(product_id))

    return response.ok
