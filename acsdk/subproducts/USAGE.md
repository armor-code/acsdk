<details><summary><code>client.get_all_subproducts()</code></summary>

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
subproducts = await client.get_all_subproducts()
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/sub-product/elastic
    ?environmentName=PRODUCTION
    &pageSize=20
    &pageNumber=0
    &tags=
    &sortBy=NAME
    &direction=ASC
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
            "id": "235781",
            "createdAtDate": 1721911018000,
            "updatedAtDate": 1721911018000,
            "createdBy": "bjenkins@armorcode.io",
            "updatedBy": "bjenkins@armorcode.io",
            "isDeleted": false,
            "isPublished": true,
            "updateSource": null,
            "tenant": 295,
            "businessUnitId": 1283,
            "name": "SUBPRODUCT_NAME",
            "description": null,
            "versionNumber": null,
            "category": null,
            "repoLink": null,
            "repoType": null,
            "technologies": "",
            "programmingLanguage": "",
            "type": null,
            "types": [],
            "origin": null,
            "businessOwner": null,
            "businessOwnerName": null,
            "businessOwnerEmail": null,
            "securityOwner": null,
            "securityOwnerName": null,
            "securityOwnerEmail": null,
            "engineeringOwner": null,
            "engineeringOwnerName": null,
            "engineeringOwnerEmail": null,
            "supportOwner": null,
            "supportOwnerName": null,
            "supportOwnerEmail": null,
            "complianceOwner": null,
            "complianceOwnerName": null,
            "complianceOwnerEmail": null,
            "teamId": null,
            "teamName": null,
            "complianceRequired": false,
            "publicCloud": true,
            "internetFacing": true,
            "parent": 202687,
            "parentName": "PRODUCT_NAME",
            "score": null,
            "risk": null,
            "confidentialityRequirement": "Not Defined",
            "confidentiality": "None",
            "availabilityRequirement": "Low",
            "availability": "None",
            "attackingVector": "Network",
            "confidentialityOptions": "",
            "impact": null,
            "likelihood": null,
            "tags": null,
            "cloneSourceSubProductId": null,
            "cloneSourceSubProductName": null,
            "errorTools": null,
            "inactiveTools": null,
            "notConfiguredTools": null,
            "severity": null,
            "status": "Active",
            "artifacts": [],
            "tagList": [],
            "tagsMetaMap": null,
            "sourceProvidedId": null,
            "tier": null,
            "riskyFinding": null,
            "unusedRecommendedTools": null,
            "riskCachedProperties": null,
            "deleted": false,
            "published": true
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

<details><summary><code>client.get_subproduct_by_id(subproduct_id)</code></summary>

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
subproduct = await client.get_subproduct_by_id(subproduct_id)
```
</td>
			<td>

```http
GET https://app.armorcode.com/api/sub-product/{{subproductId}}
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "id": "235781",
    "createdAtDate": 1721911018000,
    "updatedAtDate": 1721911018000,
    "createdBy": "bjenkins@armorcode.io",
    "updatedBy": "bjenkins@armorcode.io",
    "isDeleted": false,
    "isPublished": true,
    "updateSource": null,
    "tenant": 295,
    "businessUnitId": 1283,
    "name": "SUBPRODUCT_NAME",
    "description": null,
    "versionNumber": null,
    "category": null,
    "repoLink": null,
    "repoType": null,
    "technologies": "",
    "programmingLanguage": "",
    "type": null,
    "types": [],
    "origin": null,
    "businessOwner": null,
    "businessOwnerName": null,
    "businessOwnerEmail": null,
    "securityOwner": null,
    "securityOwnerName": null,
    "securityOwnerEmail": null,
    "engineeringOwner": null,
    "engineeringOwnerName": null,
    "engineeringOwnerEmail": null,
    "supportOwner": null,
    "supportOwnerName": null,
    "supportOwnerEmail": null,
    "complianceOwner": null,
    "complianceOwnerName": null,
    "complianceOwnerEmail": null,
    "teamId": null,
    "teamName": null,
    "complianceRequired": false,
    "publicCloud": true,
    "internetFacing": true,
    "parent": 202687,
    "parentName": "PRODUCT_NAME",
    "score": null,
    "risk": null,
    "confidentialityRequirement": "Not Defined",
    "confidentiality": "None",
    "availabilityRequirement": "Low",
    "availability": "None",
    "attackingVector": "Network",
    "confidentialityOptions": "",
    "impact": null,
    "likelihood": null,
    "tags": null,
    "cloneSourceSubProductId": null,
    "cloneSourceSubProductName": null,
    "errorTools": null,
    "inactiveTools": null,
    "notConfiguredTools": null,
    "severity": null,
    "status": "Active",
    "artifacts": [],
    "tagList": [],
    "tagsMetaMap": null,
    "sourceProvidedId": null,
    "tier": null,
    "riskyFinding": null,
    "unusedRecommendedTools": null,
    "riskCachedProperties": null,
    "deleted": false,
    "published": true
}
```

</details>

<details><summary><code>client.get_subproducts_by_name(subproduct_name)</code></summary>

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
subproducts = await client.get_subproducts_by_name(subproduct_name)
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
[
    {
        "id": "235781",
        "createdAtDate": 1721911018000,
        "updatedAtDate": 1721911018000,
        "createdBy": "bjenkins@armorcode.io",
        "updatedBy": "bjenkins@armorcode.io",
        "isDeleted": false,
        "isPublished": true,
        "updateSource": null,
        "tenant": 295,
        "businessUnitId": 1283,
        "name": "SUBPRODUCT_NAME",
        "description": null,
        "versionNumber": null,
        "category": null,
        "repoLink": null,
        "repoType": null,
        "technologies": "",
        "programmingLanguage": "",
        "type": null,
        "types": [],
        "origin": null,
        "businessOwner": null,
        "businessOwnerName": null,
        "businessOwnerEmail": null,
        "securityOwner": null,
        "securityOwnerName": null,
        "securityOwnerEmail": null,
        "engineeringOwner": null,
        "engineeringOwnerName": null,
        "engineeringOwnerEmail": null,
        "supportOwner": null,
        "supportOwnerName": null,
        "supportOwnerEmail": null,
        "complianceOwner": null,
        "complianceOwnerName": null,
        "complianceOwnerEmail": null,
        "teamId": null,
        "teamName": null,
        "complianceRequired": false,
        "publicCloud": true,
        "internetFacing": true,
        "parent": 202687,
        "parentName": "PRODUCT_NAME",
        "score": null,
        "risk": null,
        "confidentialityRequirement": "Not Defined",
        "confidentiality": "None",
        "availabilityRequirement": "Low",
        "availability": "None",
        "attackingVector": "Network",
        "confidentialityOptions": "",
        "impact": null,
        "likelihood": null,
        "tags": null,
        "cloneSourceSubProductId": null,
        "cloneSourceSubProductName": null,
        "errorTools": null,
        "inactiveTools": null,
        "notConfiguredTools": null,
        "severity": null,
        "status": "Active",
        "artifacts": [],
        "tagList": [],
        "tagsMetaMap": null,
        "sourceProvidedId": null,
        "tier": null,
        "riskyFinding": null,
        "unusedRecommendedTools": null,
        "riskCachedProperties": null,
        "deleted": false,
        "published": true
    }
]
```

</details>
