from ..util import fetch, Promise

async def delete_team_by_id(session, team_id):
    response = await fetch(session, "delete", "/api/team/" + team_id)

    return response
