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