import asyncio
from itertools import chain

from ..util import fetch, Promise

async def get_all_teams(session):
    return await (await fetch(session, "get", "/api/team/filters")).json()

async def get_team_by_id(session, team_id):
    return await (await fetch(session, "get", "/api/team/" + team_id)).json()