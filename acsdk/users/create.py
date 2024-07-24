from ..util import fetch, Promise

async def create_user(session, email):
    response = await fetch(session, "post", "/user/add/user", json={
        "email": email,
        "disableLogin": disable_login,
        "tenantRole": tenant_role,
        "teamInfo": None
    })

    return response