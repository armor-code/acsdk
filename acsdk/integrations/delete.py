import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from util import fetch, Promise

async def delete_configuration_by_id(session, configuration_id):
    # THIS URL IS FOR GIT*, NON-GIT* INSTALLATIONS WILL BE DIFFERENT
    response = await fetch(session, "delete", "/user/tools/git/gitInstallation/" + str(configuration_id))

    return response.ok
