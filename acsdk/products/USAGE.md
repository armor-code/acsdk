<details><summary><code>client.get_all_products()</code></summary>

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
products = await client.get_all_products()
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/product/elastic/paged
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
            "id": "202687",
            "createdAtDate": 1721911006000,
            "updatedAtDate": 1721911006000,
            "createdBy": "bjenkins@armorcode.io",
            "updatedBy": "bjenkins@armorcode.io",
            "isDeleted": false,
            "isPublished": true,
            "updateSource": null,
            "tenant": 295,
            "businessUnitId": 1283,
            "name": "PRODUCT_NAME",
            "type": 1,
            "types": null,
            "description": null,
            "status": "Active",
            "versionNumber": null,
            "category": null,
            "revenueImpact": null,
            "environment": null,
            "classType": "Software only",
            "hostedCloud": null,
            "complianceRequireds": null,
            "userRecords": null,
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
            "complianceRequired": true,
            "publicCloud": true,
            "internetFacing": true,
            "score": null,
            "risk": null,
            "tier": null,
            "confidentialityRequirement": "Not Defined",
            "confidentiality": "None",
            "availabilityRequirement": "Low",
            "availability": "None",
            "attackingVector": "Network",
            "confidentialityOptions": "",
            "impact": null,
            "likelihood": null,
            "tags": null,
            "slaTemplateId": null,
            "subProductCount": 1,
            "riskCalculationType": null,
            "mostRiskySubProduct": null,
            "artifacts": [],
            "tagList": [],
            "sourceProvidedId": null,
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

<details><summary><code>client.get_product_by_id(product_id)</code></summary>

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
product = await client.get_product_by_id(product_id)
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/product/{{productId}}
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "id": "202687",
    "createdAtDate": 1721911006000,
    "updatedAtDate": 1721911006000,
    "createdBy": "bjenkins@armorcode.io",
    "updatedBy": "bjenkins@armorcode.io",
    "isDeleted": false,
    "isPublished": true,
    "updateSource": null,
    "tenant": 295,
    "businessUnitId": 1283,
    "name": "PRODUCT_NAME",
    "type": 1,
    "types": null,
    "description": null,
    "status": "Active",
    "versionNumber": null,
    "category": null,
    "revenueImpact": null,
    "environment": null,
    "classType": "Software only",
    "hostedCloud": null,
    "complianceRequireds": null,
    "userRecords": null,
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
    "complianceRequired": true,
    "publicCloud": true,
    "internetFacing": true,
    "score": null,
    "risk": null,
    "tier": null,
    "confidentialityRequirement": "Not Defined",
    "confidentiality": "None",
    "availabilityRequirement": "Low",
    "availability": "None",
    "attackingVector": "Network",
    "confidentialityOptions": "",
    "impact": null,
    "likelihood": null,
    "tags": null,
    "slaTemplateId": null,
    "subProductCount": 1,
    "riskCalculationType": null,
    "mostRiskySubProduct": null,
    "artifacts": [],
    "tagList": [],
    "sourceProvidedId": null,
    "riskyFinding": null,
    "unusedRecommendedTools": null,
    "riskCachedProperties": null,
    "deleted": false,
    "published": true
}
```

</details>

<details><summary><code>client.get_products_by_name(product_name)</code></summary>

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
products = await client.get_products_by_name(product_name)
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
        "id": "202687",
        "createdAtDate": 1721911006000,
        "updatedAtDate": 1721911006000,
        "createdBy": "bjenkins@armorcode.io",
        "updatedBy": "bjenkins@armorcode.io",
        "isDeleted": false,
        "isPublished": true,
        "updateSource": null,
        "tenant": 295,
        "businessUnitId": 1283,
        "name": "PRODUCT_NAME",
        "type": 1,
        "types": null,
        "description": null,
        "status": "Active",
        "versionNumber": null,
        "category": null,
        "revenueImpact": null,
        "environment": null,
        "classType": "Software only",
        "hostedCloud": null,
        "complianceRequireds": null,
        "userRecords": null,
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
        "complianceRequired": true,
        "publicCloud": true,
        "internetFacing": true,
        "score": null,
        "risk": null,
        "tier": null,
        "confidentialityRequirement": "Not Defined",
        "confidentiality": "None",
        "availabilityRequirement": "Low",
        "availability": "None",
        "attackingVector": "Network",
        "confidentialityOptions": "",
        "impact": null,
        "likelihood": null,
        "tags": null,
        "slaTemplateId": null,
        "subProductCount": 1,
        "riskCalculationType": null,
        "mostRiskySubProduct": null,
        "artifacts": [],
        "tagList": [],
        "sourceProvidedId": null,
        "riskyFinding": null,
        "unusedRecommendedTools": null,
        "riskCachedProperties": null,
        "deleted": false,
        "published": true
    }
]
```

</details>
