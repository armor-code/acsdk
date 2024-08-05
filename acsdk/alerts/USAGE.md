<details><summary><code>client.get_all_alerts()</code></summary>

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
alerts = await client.get_all_alerts()
```
</td>
			<td>

```http
GET https://app.armorcode.com/api/alerts
    ?severity=CRITICAL,HIGH
    &page=0
    &size=10
    &sort=createdAt,desc
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "content": [
        {
            "id": "A-1",
            "severity": "MEDIUM",
            "status": "OPEN",
            "armorcodeTicketId": "null",
            "ticketUrl": null,
            "title": "1 new GITLAB repository synced for installation 11214",
            "description": "1 new GITLAB repository synced for installation 11214",
            "product": {
                "id": null,
                "name": null
            },
            "subProduct": {
                "id": null,
                "name": null
            },
            "environment": {
                "id": null,
                "name": null
            },
            "createdAt": 1718025431642,
            "updatedAt": 1718025431642,
            "assignee": {
                "id": null,
                "name": null
            },
            "sourceName": "GIT_NEW_REPO_SYNCED",
            "notificationId": null,
            "state": "UNREAD",
            "payload": "{\"installationName\":\"INSTALLATION_NAME\",\"loginId\":11214,\"installationId\":11214,\"toolName\":\"GITLAB\"}",
            "category": "Integration"
        }
    ],
    "pageable": {
        "pageNumber": 0,
        "pageSize": 100,
        "sort": {
            "empty": false,
            "sorted": true,
            "unsorted": false
        },
        "offset": 0,
        "paged": true,
        "unpaged": false
    },
    "last": true,
    "totalElements": 1,
    "totalPages": 1,
    "first": true,
    "size": 100,
    "number": 0,
    "sort": {
        "empty": false,
        "sorted": true,
        "unsorted": false
    },
    "numberOfElements": 1,
    "empty": false
}
```

</details>

<details><summary><code>client.mark_alerts_as_read(alert_ids)</code></summary>

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
await client.mark_alerts_as_read(alert_ids)
```
</td>
			<td>

```http
PUT https://app.armorcode.com/api/alerts/update
Content-Type: application/json

{
    "state": "READ",
    "id": ["1116"]
}
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```
Updated Alerts
```

</details>
