import asyncio
from itertools import chain

from .. import integrations
from ..util import fetch, Promise

async def get_all_integrations(session):
    return await (await fetch(session, "get", "/user/tools/integration-tools/status")).json()
