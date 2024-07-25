<details><summary><code>client.get_all_security_tools()</code></summary>

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
security_tools = await client.get_all_security_tools()
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/tools/appsec-tools/status
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
[
    {
        "toolName": "Snyk",
        "toolType": "SCA/SAST/Container Security/IaC",
        "toolId": "SNYK",
        "configurationStatus": "ACTIVE",
        "integrations": 1,
        "operationalStatus": "ACTIVE",
        "scanStatus": null,
        "executionDate": 1721911072000,
        "version": [],
        "isAuditEnabled": true,
        "businessUnitId": null,
        "tenant": null,
        "productId": null,
        "subProductId": null,
        "isShareable": true,
        "operationalStatusMessage": "",
        "activeCount": 1,
        "inactiveCount": 0,
        "configErrorCount": 0
    }
]
```

</details>
