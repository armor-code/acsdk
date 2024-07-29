import asyncio
from itertools import chain

from ..util import fetch, Promise

async def get_all_installations_by_tool_name(session, tool_name):
    # THIS URL IS FOR GIT*, NON-GIT* INSTALLATIONS WILL BE DIFFERENT
    response = await fetch(session, "get", "/user/tools/git/gitInstallation/repoType/" + str(tool_name))

    return await response.json()
