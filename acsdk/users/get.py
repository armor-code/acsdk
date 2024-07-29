import asyncio
from itertools import chain

from ..util import fetch, Promise

async def get_all_users(session):
    # `/user/get-users` also exists but has less data
    return await (await fetch(session, "get", "/user/data/users")).json()

async def get_user_by_id(session, user_id):
    user = list(filter(lambda user: user["id"] == user_id, await get_all_users(session)))

    return user