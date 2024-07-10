import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from ..util import fetch, Promise

async def create_subproduct(session, product_id, subproduct_name, subproduct_payload={}):
    # FIXME: Replace this shallow merge with a deep merge.
    subproduct = await (await fetch(session, "post", "/api/sub-product", json={
        "environments": [
            {
                "name": "Production",
                "branch": "master",
                "url": ""
            },
            {
                "name": "Staging",
                "branch": "master",
                "url": ""
            }
        ],
        "engineeringOwner": None,
        "securityOwner": None,
        "businessOwner": None,
        "complianceOwner": None,
        "supportOwner": None,
        "confidentialityRequirement": "Not Defined",
        "availabilityRequirement": "Low",
        "availability": "None",
        "attackingVector": "Network",
        "publicCloud": True,
        "internetFacing": True,
        "product": {
            "id": product_id
        },
        "name": subproduct_name,
        "types": [],
        "status": "Active",
        "programmingLanguage": "",
        "technologies": "",
        "slaTemplateId": None,
        "confidentiality": "NONE",
        "confidentialityOptions": "",
        **subproduct_payload
    })).json()

    return subproduct["id"]
