import asyncio
from itertools import chain

from ..util import fetch, Promise


async def create_configuration(session, configuration):
    configuration = await (await fetch(session, "post", "/user/tools/git/gitInstallation", json=configuration)).json()

    return configuration["id"]
