from ..util import fetch, Promise

async def update_team_by_id(session, team_id):
    # TODO:
    team_payload = await get_team_by_id(team_id)

    response = await fetch(session, "put", "/api/team/with-user", json={
        "name": "My New Team 2",
        "description": "",
        "members": [],
        "properties": [
            {
                "businessUnitId": 2255,
                "businessUnitName": "Default Organization",
                "productSubProductMap": [],
                "accessOnAllProduct": true,
                "groups": [],
                "accessType": "individual",
                "members": []
            }
        ],
        "approvalWorkflow": {
            "approvers": []
        },
        "emailAlias": "",
        "msTeamsLoginId": null,
        "msTeamsChannel": [],
        "accessOnAllBusinessUnits": false,
        "id": team_id
    })

    return response
