<details><summary><code>client.get_all_integrations()</code></summary>

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
integrations = await client.get_all_integrations()
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/tools/integration-tools/status
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
[
    {
        "toolName": "APIKEY",
        "toolType": "INTEGRATION",
        "toolId": "APIKEY",
        "configurationStatus": "ACTIVE",
        "integrations": 1,
        "operationalStatus": "ACTIVE",
        "scanStatus": null,
        "executionDate": 1717766692000,
        "version": null,
        "isAuditEnabled": false,
        "businessUnitId": null,
        "tenant": null,
        "productId": null,
        "subProductId": null,
        "isShareable": null,
        "operationalStatusMessage": null,
        "activeCount": 1,
        "inactiveCount": 0,
        "configErrorCount": 0
    }
]
```

</details>
