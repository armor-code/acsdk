from ..util import fetch, Promise

async def delete_user_by_id(session, user_id):
    response = await fetch(session, "delete", "/user/data/remove/" + user_id)

    return response