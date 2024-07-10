import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

async def get_all_teams(session):
    return await (await fetch(session, "get", "/api/team/filters")).json()
