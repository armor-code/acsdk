import asyncio
from itertools import chain
import math

from ..util import fetch, Promise


def _get_findings(session, after_key=None, partial_findings_search_payload=None):
    return fetch(
        session,
        "post",
        "/api/findings/",
        params=list({"afterKey": after_key}.items()),
        json={
            "filters": {},
            "ignoreDuplicate": True,
            "ignoreMitigated": None,
            "sort": "",
            # "sortColumns": [],
            "ticketStatusRequired": True,
            **(partial_findings_search_payload if partial_findings_search_payload is not None else {}),
            # **({"afterKey": after_key} if after_key is not None else {}),
            # "size": 100,
        },
    )


async def get_all_findings(session, partial_findings_search_payload=None):
    response = await (
        await fetch(
            session,
            "post",
            "/user/findings/",
            json={
                "filters": {},
                "ignoreDuplicate": True,
                "ignoreMitigated": None,
                "sort": "",
                "sortColumns": [],
                "ticketStatusRequired": True,
                **(partial_findings_search_payload if partial_findings_search_payload is not None else {}),
                "size": 10,
            },
        )
    ).json()

    findings = response["content"]

    total_pages = math.ceil(response["totalPages"] / 100)

    if total_pages >= 1:
        for _ in range(1, total_pages):
            response = await (await _get_findings(session, findings[-1]["id"], partial_findings_search_payload)).json()

            findings.extend(response["data"]["findings"])

    return findings


async def get_finding_by_id(session, finding_id):
    return await (await fetch(session, "get", "/user/findings/" + str(finding_id))).json()


def _get_findings_by_saved_search_id(
    session,
    saved_search_id,
    page_number=None,
):
    return fetch(
        session,
        "get",
        "/user/findings/saved-search/" + str(saved_search_id),
        params=list(
            {
                "size": "100",
                **({"page": str(page_number)} if page_number is not None else {}),
            }.items()
        ),
    )


def _clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))


# TODO: Switch to using `/api/savedSearch/findings`?
async def get_all_findings_by_saved_search_id(session, saved_search_id):
    response = await (await _get_findings_by_saved_search_id(session, saved_search_id)).json()

    total_pages = _clamp(0, response["totalPages"], 100)

    tasks = []

    if total_pages >= 1:
        for page_number in range(1, total_pages):
            tasks.append(
                asyncio.create_task(
                    Promise.reduce_series(
                        [
                            _get_findings_by_saved_search_id(session, saved_search_id, page_number),
                            lambda response: response.json(),
                            lambda data: data["content"],
                        ]
                    )
                )
            )

    findings = response["content"]

    pages = await asyncio.gather(*tasks)

    findings.extend(chain.from_iterable(pages))

    return findings


async def get_all_findings_by_subproduct_id(session, subproduct_id, partial_findings_search_payload=None):
    return await get_all_findings(session, partial_findings_search_payload)
