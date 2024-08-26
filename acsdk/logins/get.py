import asyncio
from itertools import chain
import math

from ..tool_map import tool_map
from ..util import fetch, Promise, match_fuzzy


async def get_all_logins_by_tool_name(session, tool_name):
    if tool_name.startswith("Custom-"):
        return "/user/tools/generic/login_details/" + tool_name

    endpoint = next((value for key, value in tool_map.items() if key.casefold() == tool_name.casefold()), None)

    # At some point we will need to distinguish between `API`, `Push script` and `Scan upload`
    if isinstance(endpoint, dict):
        if "API" in endpoint:
            endpoint = endpoint["API"]
        elif "WebHook" in endpoint:
            endpoint = endpoint["WebHook"]
        elif "Push script" in endpoint:
            endpoint = endpoint["Push script"]
        # elif "Scan upload" in endpoint:
        #   endpoint = endpoint["Scan upload"]
        else:
            print(endpoint)
            # raise Exception()
            return []

    method, url = endpoint.split()

    response = await (await fetch(session, method.lower(), url)).json()

    if "configurations" in response:
        return response["configurations"]

    return response


def _get_mappings_by_login_id(session, tool_name, login_id, tool_type, page_number=None):
    return fetch(
        session,
        "post",
        "/user/tools/generic/configurations/" + str(tool_name),
        json={
            **({"page": str(page_number)} if page_number is not None else {}),
            "size": 10,
            "sort": "createdAt,desc",
            "sortOrder": "desc",
            "sortColumn": "createdAt",
            "filters": {},
            "toolType": tool_type,
            "loginId": login_id,
            "toolFilters": {},
        },
        # THIS CALL IS IDEMPOTENT
        retry=True,
    )


async def get_all_mappings_by_login_id(session, tool_name, login_id, tool_type="PULL"):
    response = await (await _get_mappings_by_login_id(session, tool_name, login_id, tool_type)).json()

    total_pages = math.ceil(response["totalElements"] / 10)

    tasks = []

    if total_pages >= 1:
        for page_number in range(1, total_pages):
            tasks.append(
                asyncio.create_task(
                    Promise.reduce_series(
                        [
                            _get_mappings_by_login_id(session, tool_name, login_id, tool_type, page_number),
                            lambda response: response.json(),
                            lambda data: data["configurations"],
                        ]
                    )
                )
            )

    mappings = response["configurations"]

    pages = await asyncio.gather(*tasks)

    mappings.extend(chain.from_iterable(pages))

    return mappings


def _get_projects_by_login_id(session, tool_name, login_id):
    # This endpoint doesn't appear to respect pagination parameters
    return fetch(
        session,
        "get",
        "/user/tools/generic/configurations/" + tool_name + "/project",
        params=list({"login_id": login_id}.items()),
    )


async def get_all_projects_by_login_id(session, tool_name, login_id):
    return (await (await _get_projects_by_login_id(session, tool_name, login_id)).json())["projects"]


async def get_all_unmapped_projects_by_login_id(session, tool_name, login_id):
    # TODO: Parallelize
    projects = await get_all_projects_by_login_id(session, tool_name, login_id)

    mappings = await get_all_mappings_by_login_id(session, tool_name, login_id)

    unmapped_projects = [
        project for project in projects if not any(project["id"] == mapping["siteId"] for mapping in mappings)
    ]

    return unmapped_projects


async def get_project_by_name(session, tool_name, login_id, project_name):
    projects = await get_all_mappings_by_login_id(session, tool_name, login_id)

    return list(filter(lambda project: match_fuzzy(project["name"], project_name), projects))
