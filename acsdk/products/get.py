import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

def _get_products(session, page_number=None):
    return fetch(session, "get", "/user/product/elastic/paged", params=list({
        "environmentName": "PRODUCTION",
        "pageSize": "20",
        **({"pageNumber": str(page_number)} if page_number is not None else {}),
        "tags": "",
        "sortBy": "NAME",
        "direction": "ASC"
    }.items()))

async def get_all_products(session):
    response = await (await _get_products(session)).json()

    total_pages = response["totalPages"]

    tasks = []

    if total_pages > 1:
        for page_number in range(1, total_pages):
            tasks.append(asyncio.create_task(Promise.reduce_series([
                _get_products(session, page_number),
                lambda response: response.json(),
                lambda data: data["content"]
            ])))

    products = response["content"]

    pages = await tqdm.gather(*tasks)

    products.extend(chain.from_iterable(pages))

    return products

async def get_product_by_id(session, product_id):
    return await (await fetch(session, "get", "/user/product/" + str(product_id))).json()

async def get_products_by_name(session, product_name):
    products = list(filter(lambda product: product["name"].casefold() == product_name.casefold(), await get_all_products(session)))

    if len(products) > 1:
        print("WARN: Multiple matches for product name: " + product_name)

    return products
