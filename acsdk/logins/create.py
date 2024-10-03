import asyncio
from itertools import chain

from ..util import fetch, Promise


async def create_login(session, tool_name, configuration):
    # A login only needs to be created for `tool_type="PULL"`

    return await (
        await fetch(
            session,
            "post",
            "/user/tools/generic/login_details/" + tool_name,
            json=configuration,
        )
    ).json()
