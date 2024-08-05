<details><summary><code>client.get_all_teams()</code></summary>

#### Example:

<table>
	<tbody>
		<tr>
			<th width="441"><strong>Python</strong></td>
			<th width="441"><strong>REST</strong></td>
		</tr>
		<tr>
			<td>

```python
teams = await client.get_all_teams()
```
</td>
			<td>

```http
GET https://app.armorcode.com/api/team/filters
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "name": [
        {
            "id": 16635,
            "name": "All Armorcode Users"
        }
    ]
}
```

</details>

<details><summary><code>client.get_team_by_id(team_id)</code></summary>

#### Example:

<table>
	<tbody>
		<tr>
			<th width="441"><strong>Python</strong></td>
			<th width="441"><strong>REST</strong></td>
		</tr>
		<tr>
			<td>

```python
team = await client.get_team_by_id(team_id)
```
</td>
			<td>

```http
GET https://app.armorcode.com/api/team/{{teamId}}
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "id": 16635,
    "createdAt": 1717766578000,
    "updatedAt": 1717766578000,
    "createdBy": "bjenkins@armorcode.io",
    "updatedBy": "bjenkins@armorcode.io",
    "isDeleted": false,
    "isPublished": true,
    "tenant": 295,
    "name": "All Armorcode Users",
    "description": "Default Team giving users initial access to ArmorCode with the scope of all Organizations. Both the name and scope of access can be configured. The assigned roles of a user added to the Team controls the actions available within the scope.",
    "level": null,
    "properties": [],
    "members": [],
    "lead": null,
    "hasAccess": null,
    "emailAlias": null,
    "slackConfigId": null,
    "msTeamsLoginId": null,
    "msTeamsTeam": null,
    "msTeamsChannel": null,
    "accessOnAllBusinessUnits": true,
    "approvalWorkflow": null,
    "deleted": false,
    "published": true,
    "tags": null,
    "securityOwner": null,
    "complianceOwner": null,
    "engineeringOwner": null,
    "supportOwner": null,
    "businessOwner": null
}
```

</details>
