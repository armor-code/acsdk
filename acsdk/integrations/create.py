import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

async def create_configuration(session, configuration_name, configuration_token, configuration_host_url, configuration_repository_type):
    configuration = await (await fetch(session, "post", "/user/tools/git/gitInstallation", json={
        "name": "My GitLab Configuration",
        "token": "glpat-X3bkjQaBmzzUKDq3ose8",
        "hostUrl": "https://gitlab.com",
        "repoType": "GITLAB"
    })).json()

    return configuration["id"]
