import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from ..util import fetch, Promise, match_fuzzy

async def get_all_logins_by_tool_name(session, tool_name):
    return (await (await fetch(session, "get", "/user/tools/generic/login_details/" + str(tool_name))).json())["configurations"]

async def get_all_mappings_by_login_id(session, tool_name, login_id):
    # WARN: This is a paginated endpoint and we are only getting the first page.
    return (await (await fetch(session, "post", "/user/tools/generic/configurations/" + str(tool_name), json={
        "page": 0,
        "size": 10,
        "sort": "createdAt,desc",
        "sortOrder": "desc",
        "sortColumn": "createdAt",
        "filters": {},
        "toolType":"PULL",
        "loginId": login_id,
        "toolFilters": {}
    })).json())["configurations"]

def get_projects_by_login_id(session, toolName, login_id, page_number = 0, **kwargs):
    # Not implemented because this endpoint doesn't appear to respect pagination parameters
    pass

async def get_project_by_name(session, tool_name, login_id, project_name):
    return list(filter(lambda project: match_fuzzy(project["name"], project_name), await get_all_mappings_by_login_id(session, tool_name, login_id)))

async def get_all_projects_by_login_id(session, tool_name, login_id):
    # This endpoint doesn't appear to respect pagination parameters
    response = await fetch(session, "get", "/user/tools/generic/configurations/" + tool_name + "/project", params=list({
        "login_id": login_id
    }.items()))

    data = await response.json()

    return data["projects"]
