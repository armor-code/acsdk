import asyncio
from itertools import chain

from ..util import fetch, Promise, match_fuzzy


def _get_subproducts(session, page_number=None):
    return fetch(
        session,
        "get",
        "/user/sub-product/elastic",
        params=list(
            {
                "environmentName": "PRODUCTION",
                "pageSize": "100",
                **({"pageNumber": str(page_number)} if page_number is not None else {}),
                "tags": "",
                "sortBy": "NAME",
                "direction": "ASC",
            }.items()
        ),
    )


async def get_all_subproducts(session):
    response = await (await _get_subproducts(session)).json()

    total_pages = response["totalPages"]

    tasks = []

    if total_pages > 1:
        for page_number in range(1, total_pages):
            tasks.append(
                asyncio.create_task(
                    Promise.reduce_series(
                        [
                            _get_subproducts(session, page_number),
                            lambda response: response.json(),
                            lambda data: data["content"],
                        ]
                    )
                )
            )

    subproducts = response["content"]

    pages = await asyncio.gather(*tasks)

    subproducts.extend(chain.from_iterable(pages))

    return subproducts


async def get_subproduct_by_id(session, subproduct_id):
    return await (
        await fetch(
            session, "get", "/api/sub-product/" + str(subproduct_id), params=list({"environment": "Production"}.items())
        )
    ).json()


async def get_subproducts_by_name(session, subproduct_name):
    subproducts = list(
        filter(
            lambda subproduct: match_fuzzy(
                subproduct["name"],
                subproduct_name,
            ),
            await get_all_subproducts(session),
        )
    )

    if len(subproducts) > 1:
        print("WARN: Multiple matches for subproduct name: " + subproduct_name)

    return subproducts


def get_all_subproducts_by_product_id(session, product_id):
    # TODO
    pass
