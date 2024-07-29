import asyncio
from itertools import chain

from ..util import fetch, Promise

def _get_findings(session, page_number=None, **kwargs):
    return fetch(session, "post", "/user/findings/", json={
        "filters": {},
        "ignoreDuplicate": True,
        "ignoreMitigated": None,
        "sort": "",
        "sortColumns": [],
        "ticketStatusRequired": True,
        **(kwargs.get("json") if kwargs.get("json") is not None else {}),
        **({'page': str(page_number)} if page_number is not None else {}),
        "size": 100
    })

def _clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

async def get_all_findings(session, **kwargs):
    response = await (await _get_findings(session, **kwargs)).json()

    total_pages = _clamp(0, response["totalPages"], 100)

    tasks = []

    if total_pages >= 1:
        for page_number in range(1, total_pages):
            tasks.append(asyncio.create_task(Promise.reduce_series([
                _get_findings(session, page_number, **kwargs),
                lambda response: response.json(),
                lambda data: data["content"]
            ])))

    findings = response["content"]

    pages = await asyncio.gather(*tasks)

    findings.extend(chain.from_iterable(pages))

    return findings

async def get_finding_by_id(session, finding_id):
    return await (await fetch(session, "get", "/user/findings/" + str(finding_id))).json()

def _get_findings_by_saved_search_id(session, saved_search_id, page_number=None,):
    return fetch(session, "get", "/user/findings/saved-search/" + str(saved_search_id), params=list({
        "size": "100",
        **({"page": str(page_number)} if page_number is not None else {}),
    }.items()))

async def get_all_findings_by_saved_search_id(session, saved_search_id):
    response = await (await _get_findings_by_saved_search_id(session, saved_search_id)).json()

    total_pages = _clamp(0, response["totalPages"], 100)

    tasks = []

    if total_pages >= 1:
        for page_number in range(1, total_pages):
            tasks.append(asyncio.create_task(Promise.reduce_series([
                _get_findings_by_saved_search_id(session, saved_search_id, page_number),
                lambda response: response.json(),
                lambda data: data["content"]
            ])))

    findings = response["content"]

    pages = await asyncio.gather(*tasks)

    findings.extend(chain.from_iterable(pages))

    return findings
