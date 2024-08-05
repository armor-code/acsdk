import asyncio
from itertools import chain

from ..util import fetch, Promise

async def mark_alerts_as_read(session, alert_ids):
    response = await fetch(session, "put", "/api/alerts/update", json={
        "state":"READ",
        "id": alert_ids
    })

    return response.ok
