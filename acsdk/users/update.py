from ..util import fetch, Promise

async def update_user_by_id(session, user_id):
    # TODO:
    user_payload = await get_user_by_id(user_id)

    response = await fetch(session, "put", "/user/add/user", json={
        "email": email,
        "disableLogin": true,
        "teamInfo": [
            {
                "teamName": "My New Team",
                "teamId": 18517,
                "properties": [],
                "role": "Executive",
                "canBeModified": true
            }
        ],
        "id": user_id
    })

    return response
