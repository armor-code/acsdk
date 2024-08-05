<details><summary><code>client.get_all_users()</code></summary>

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
users = await client.get_all_users()
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/data/users
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
[
    {
        "userId": 3692,
        "email": "bjenkins@armorcode.io",
        "tenantRole": "ROLE_TENANTADMIN",
        "name": "Brian Jenkins",
        "data": null,
        "canBeModified": true,
        "disableLogin": false,
        "isBasicAuthEnabled": false,
        "lastlogin": 1721910574000,
        "teamInfo": null,
        "defaultBu": null
    }
]
```

</details>

<details><summary><code>client.get_user_by_id(user_id)</code></summary>

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
user = await client.get_user_by_id(user_id)
```
</td>
			<td>

```http
N/A
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "userId": 3692,
    "email": "bjenkins@armorcode.io",
    "tenantRole": "ROLE_TENANTADMIN",
    "name": "Brian Jenkins",
    "data": null,
    "canBeModified": true,
    "disableLogin": false,
    "isBasicAuthEnabled": false,
    "lastlogin": 1721910574000,
    "teamInfo": null,
    "defaultBu": null
}
```

</details>
