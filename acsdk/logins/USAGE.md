<details><summary><code>client.get_all_logins_by_tool_name()</code></summary>

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
logins = await client.get_all_logins_by_tool_name(tool_name)
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/tools/generic/login_details/{{tool_name}}
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "configurations": [
        {
            "name": "CONFIGURATION_NAME",
            "shareable": false,
            "id": 51704,
            "total_configurations": 1,
            "status": "ENABLED",
            "apiEndpoint": "https://api.snyk.io/",
            "bot_id": null,
            "expires_in": null,
            "refresh_expires_in": null,
            "scope": null,
            "token_type": null
        }
    ]
}
```

</details>

<details><summary><code>client.get_all_mappings_by_login_id(tool_name, login_id)</code></summary>

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
mappings = await client.get_all_mappings_by_login_id(tool_name, login_id)
```
</td>
			<td>

```http
POST https://app.armorcode.com/user/tools/generic/configurations/{{toolName}}
Content-Type: application/json

{
    "size": 10,
    "sort": "createdAt,desc",
    "sortOrder": "desc",
    "sortColumn": "createdAt",
    "filters": {},
    "toolType": "PULL",
    "loginId": {{loginId}},
    "toolFilters": {}
}
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "configurations": [
        {
            "id": 1120009,
            "tool_name": "Snyk",
            "product_name": "PRODUCT_NAME",
            "product_id": 202687,
            "sub_product_id": 235781,
            "sub_product_name": "SUBPRODUCT_NAME",
            "environment": "Production",
            "suspended": false,
            "operationalStatus": "ACTIVE",
            "lastConnected": 1721911072000,
            "scanStatus": "PASSED",
            "scanLastRun": 1721853107275,
            "scanNextRun": 1721914671989,
            "scanId": 946109,
            "login_id": 51704,
            "lastToolScanDate": 1721853107275,
            "metaDetails": null,
            "lastToolAssessmentDate": null,
            "latestIngestionFailureTime": null,
            "frequency": 2,
            "frequencyUnit": "DAYS",
            "engagementId": null,
            "webhookEnabled": null,
            "displayName": null,
            "exploitMaturity": "",
            "orgId": "75ab4acb-f7b0-4531-9066-4105ac959a82",
            "orgName": "ORGANIZATION_NAME",
            "origin": "",
            "project_type": "project",
            "projectId": "PROJECT_ID",
            "projectName": "PROJECT_NAME",
            "scanType": "",
            "tags": null,
            "targetId": "6b88e0d1-9cdc-4c50-93f2-f3fb2d0e29cd"
        }
    ],
    "totalElements": 1
}
```

</details>

<details><summary><code>client.get_all_projects_by_login_id(tool_name, login_id)</code></summary>

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
projects = await client.get_all_projects_by_login_id(tool_name, login_id)
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/tools/generic/configurations/{{toolName}}/project
    ?login_id={{loginId}}
    &page=0

```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "projects": [
        {
            "name": "TheRedHatter/hello-world",
            "id": "TheRedHatter/hello-world",
            "mappedStatus": null,
            "versions": null,
            "projectStatus": null,
            "otherProperties": {
                "orgId": "75ab4acb-f7b0-4531-9066-4105ac959a82",
                "orgName": "ORGANIZATION_NAME",
                "origin": "github",
                "projectStatus": "ACTIVE",
                "references": [
                    "master"
                ],
                "actualProjectId": "ca50e06b-d026-435a-8a9e-f7c123a5199a",
                "targetId": "6b88e0d1-9cdc-4c50-93f2-f3fb2d0e29cd",
                "displayName": "TheRedHatter/hello-world",
                "tags": "{\"snyk.projecttarget\":[\"theredhatter/hello-world\"],\"snyk.origin\":[\"github\"],\"snyk.projectowner\":[\"theredhatter\"],\"snyk.projecttype\":[\"sast\"],\"snyk.orgname\":[\"organization name\"],\"snyk.projectrepourl\":[\"https://github.com/theredhatter/hello-world\"],\"snyk.targetreference\":[\"master\"]}"
            },
            "tags": null
        }
    ],
    "page": 1,
    "total": 1,
    "next": false,
    "isListFromCachedProjects": null,
    "message": null,
    "pageAfter": null
}
```

</details>
