import asyncio
from itertools import chain
from tqdm.asyncio import tqdm

from util import fetch, Promise

async def create_product(session, product_name, product_payload={}):
    # FIXME: Replace this shallow merge with a deep merge.
    product = await (await fetch(session, "post", "/user/product", json={
        "classType": "Software only",
        "type": {
            "id": 1
        },
        "publicCloud": True,
        "internetFacing": True,
        "complianceRequired": True,
        "confidentialityRequirement": "Not Defined",
        "availabilityRequirement": "Low",
        "availability": "None",
        "attackingVector": "Network",
        "name": product_name,
        "status": "Active",
        "slaTemplateId": None,
        "confidentiality": "NONE",
        "confidentialityOptions": "",
        **product_payload 
    })).json()

    return product["id"]
