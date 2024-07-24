from ..util import fetch, Promise

async def create_team(session, team_name):
    response = await fetch(session, "post", "/api/team", json={
        "name": team_name,
        "description": "",
        "members": [],
        "properties": [
            {
                "businessUnitId": 2255,
                "businessUnitName": "Default Organization",
                "productSubProductMap": [],
                "accessOnAllProduct": True,
                "accessType": "individual",
                "groups": []
            }
        ],
        "approvalWorkflow": {
            "approvers": []
        },
        "emailAlias": ""
    })

    return response
