import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

def _get_alerts(session, page_number=None):
    return fetch(session, "get", "/api/alerts", params={
        #"severity": "CRITICAL,HIGH",
        "page": 0,
        "size": 10,
        "sort": "createdAt,desc"
    }.items())

async def get_all_alerts(session):
    response = await (await _get_alerts(session)).json()

    total_pages = response["totalPages"]

    tasks = []

    if total_pages > 1:
        for page_number in range(1, total_pages):
            tasks.append(asyncio.create_task(Promise.reduce_series([
                _get_alerts(session, page_number),
                lambda response: response.json(),
                lambda data: data["content"]
            ])))

    alerts = response["content"]

    pages = await tqdm.gather(*tasks)

    alerts.extend(chain.from_iterable(pages))

    return alerts
