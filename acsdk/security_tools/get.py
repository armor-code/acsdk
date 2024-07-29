import asyncio
from itertools import chain

from ..util import fetch, Promise

async def get_all_security_tools(session):
    response = await fetch(session, "get", "/user/tools/appsec-tools/status")

    return await response.json()
