<!-- <img height="128px" width="128px" align="right" /> -->

# ArmorCode Python SDK

> [!WARNING]
> This is a beta release. Not all features are available and API stability is not yet guaranteed.

<table>
	<thead>
		<tr>
			<th align="center"><strong>Contents</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<ol>
					<li><a href="#getting-started">Getting Started</a></li>
					<ol>
						<li><a href="#install">Install</a></li>
						<li><a href="#minimal-example">Minimal Example</a></li>
					</ol>
					<li><a href="#api">API</a></li>
					<ol>
						<li><a href="#alerts">Alerts</a></li>
						<li><a href="#findings">Findings</a></li>
						<li><a href="#integrations">Integrations</a></li>
						<li><a href="#security-tools">Security Tools</a></li>
						<li><a href="#logins">Logins</a></li>
						<li><a href="#products">Products</a></li>
						<li><a href="#sub-products">Sub-products</a></li>
						<li><a href="#teams">Teams</a></li>
						<li><a href="#users">Users</a></li>
					</ol>
					<li><a href="#advanced-usage">Advanced Usage</a></li>
				</ol>
			</td>
		</tr>
	</tbody>
</table>


## Getting Started

### Install

```sh
python -m pip install --user git+https://github.com/armor-code/acsdk
```

### Minimal Example

> [!Note]
> This expects the [ArmorCode API key](https://support.armorcode.com/hc/en-us/articles/19447589108499-Generating-ArmorCode-API-Key) to be supplied as an environment variable or as a file.

```python
import asyncio
import os
from pathlib import Path

from acsdk import ArmorCodeClient

async def main(api_key):
    client = ArmorCodeClient(api_key)

    products = await client.get_all_products()

    print(products)

    await client.close()

if __name__ == "__main__":
    api_key_path = os.path.normpath(os.path.join(Path(__file__).parent.absolute(), "ArmorCode_API_key.txt"))

    api_key = os.getenv("ARMORCODE_API_KEY").strip() #open(api_key_path, "r").read().strip()

    loop = asyncio.new_event_loop()

    loop.run_until_complete(main(api_key))

    loop.close()
```

## API

### Alerts

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

### Findings

<details><summary><code>client.get_all_findings()</code></summary>

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
findings = await client.get_all_findings()
```
</td>
			<td>

```http
POST https://app.armorcode.com/user/findings/
Content-Type: application/json

{
    "filters": {},
    "ignoreDuplicate": true,
    "ignoreMitigated": null,
    "sort": "",
    "sortColumns": [],
    "ticketStatusRequired": true,
    "page": 0,
    "size": 100
}
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
            "ruleId": [
                "1.327",
                "1.20"
            ],
            "mitigation": "Patched version: 4.2.2",
            "impact": null,
            "stepsToReproduce": null,
            "description": "Versions 4.2.1 and earlier of `jsonwebtoken` are affected by a verification bypass vulnerability. This is a result of weak validation of the JWT algorithm type, occuring when an attacker is allowed to arbitrarily specify the JWT algorithm.\n\n\n\n\n## Recommendation\n\nUpdate to version 4.2.2 or later.\n\n ### References: \n- https://nvd.nist.gov/vuln/detail/CVE-2015-9235\n- https://github.com/auth0/node-jsonwebtoken/commit/1bb584bc382295eeb7ee8c4452a673a77a68b687\n- https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/\n- https://github.com/advisories/GHSA-c7hr-j4mj-j2w6\n- https://www.npmjs.com/advisories/17\n- https://www.timmclean.net/2015/02/25/jwt-alg-none.html",
            "source": "Dependabot",
            "severity": "CRITICAL",
            "armorcodeCategory": "Secrets",
            "findingCategory": "Vulnerability",
            "category": "Vulnerability",
            "status": "OPEN",
            "productStatus": "Active",
            "subProductStatuses": "Active",
            "id": 659573042,
            "tid": 161,
            "policy": null,
            "lastUpdated": 1717526668000,
            "createdAt": 1715361339000,
            "externalMappings": {},
            "title": "jsonwebtoken : = 0.4.0 - Verification Bypass in jsonwebtoken",
            "armorcodeTicket": [],
            "toolSeverity": "CRITICAL",
            "cwe": [
                "20"
            ],
            "cve": [
                "CVE-2015-9235"
            ],
            "product": {
                "id": 158036,
                "name": "PRODUCT_NAME"
            },
            "subProduct": {
                "id": 346991,
                "name": "SUBPRODUCT_NAME"
            },
            "environment": {
                "id": 679687,
                "name": "Production"
            },
            "securityOwner": {
                "id": null,
                "name": null
            },
            "owner": {
                "id": null,
                "name": null
            },
            "developer": "bjenkins-armorcode@gmail.com",
            "developerName": "Brian Jenkins",
            "toolId": "RVA_kwDOLpS_Gc8AAAABR2PYgQ",
            "filePath": "package.json",
            "url": "https://github.com/bjenkins-armorcode/juice-shop/security/dependabot/1",
            "lineNumber": null,
            "mitigated": false,
            "scan": 19280155,
            "scanType": [
                "SCA"
            ],
            "analysisType": "STATIC",
            "similarFindings": null,
            "additionalDetails": {
                "COMMIT_MESSAGE": "Import juice-shop",
                "FIXED_BY_DEVELOPER_EMAIL": "bjenkins-armorcode@gmail.com",
                "isCISAKEV": false,
                "FIXED_COMMIT_MESSAGE": "Import juice-shop",
                "cvssVectorV2": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                "COMMIT_URL": "https://github.com/bjenkins-armorcode/juice-shop/commit/71513add1e6e56dc66395fdc7f405e7eb8953d31",
                "cvssVectorV3": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                "epssScore": 0.75142,
                "repositoryName": "bjenkins-armorcode/juice-shop",
                "FIXED_COMMIT_URL": "https://github.com/bjenkins-armorcode/juice-shop/commit/71513add1e6e56dc66395fdc7f405e7eb8953d31",
                "componentFixVersions": "4.2.2",
                "repositoryUrl": "https://github.com/bjenkins-armorcode/juice-shop",
                "cveUsed": "CVE-2015-9235",
                "aeName": "Production",
                "exploited": false,
                "FIXED_BY_DEVELOPER_NAME": "Brian Jenkins",
                "dateSource": "tool",
                "scanType": "SCA",
                "toolFindingStatus": "OPEN",
                "category": "Vulnerability",
                "aatiScore": 8.04,
                "toolStatusOriginal": "OPEN",
                "cvePublishedDate": 1527625740000,
                "cveLastModifiedVulDate": 1570662900000
            },
            "slaBreached": true,
            "unsupressTime": null,
            "componentName": "jsonwebtoken",
            "componentVersion": "= 0.4.0",
            "slaDueDate": 1715019036000,
            "triageDueDate": 1714587036000,
            "remediationDueDate": null,
            "underReview": null,
            "proposedData": null,
            "tagsMetaMap": {
                "SUBPRODUCT": []
            },
            "team": {
                "id": null,
                "name": null
            },
            "tags": [],
            "foundOn": 1714414236000,
            "foundOnDate": 1714414236000,
            "baseScore": 9.8,
            "impactScore": 5.9,
            "exploitabilityScore": 3.9,
            "publishedDate": 1527625740000,
            "lastModifiedDate": 1570662900000,
            "issueResolved": null,
            "toolFindingStatus": "OPEN",
            "toolStatusOriginal": null,
            "cvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
            "newUrl": null,
            "findingScore": 5.1,
            "riskScore": null,
            "armorcodeProjects": null,
            "vendor": null,
            "subProductVersion": null,
            "productVersion": null,
            "mitigatedAt": null,
            "lastTriagedDate": null,
            "lastConfirmDate": null,
            "lastFalsePositiveDate": null,
            "lastOpenDate": 1715361339930,
            "lastAcceptRiskDate": null,
            "lastSuppressDate": null,
            "lastSeenDate": 1715299200000,
            "lastTriagedDateTime": null,
            "lastConfirmDateTime": null,
            "lastFalsePositiveDateTime": null,
            "lastOpenDateTime": 1715361339000,
            "lastAcceptRiskDateTime": null,
            "lastSuppressDateTime": null,
            "lastControlledDateTime": null,
            "lastInProgressDateTime": null,
            "lastTriageDateTime": null,
            "indirectExportFields": null,
            "assetScore": null,
            "comments": null,
            "history": null,
            "exploitMetaInfo": null,
            "attachments": null,
            "tagsUsedForAssetScore": [],
            "versionFindingsCount": null,
            "correlatedFindingsCount": null,
            "vmHostIpAddresses": null,
            "riskRegisters": null,
            "ctiScore": null,
            "cwesStrings": [
                "CWE-20"
            ],
            "assessment": []
        }
    ],
    "pageable": {
        "pageNumber": 0,
        "pageSize": 100,
        "sort": {
            "sorted": true,
            "empty": false,
            "unsorted": false
        },
        "offset": 0,
        "paged": true,
        "unpaged": false
    },
    "last": false,
    "totalElements": 1,
    "totalPages": 1,
    "first": true,
    "size": 100,
    "number": 0,
    "sort": {
        "sorted": true,
        "empty": false,
        "unsorted": false
    },
    "numberOfElements": 1,
    "empty": false
}
```

</details>

<details><summary><code>client.get_finding_by_id(finding_id)</code></summary>

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
finding = await client.get_finding_by_id(finding_id)
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/findings/{{finding_id}}
```
</td>
		</tr>
	</tbody>
</table>

#### Response:

```json
{
    "ruleId": [
        "1.327",
        "1.20"
    ],
    "mitigation": "Patched version: 4.2.2",
    "impact": null,
    "stepsToReproduce": null,
    "description": "Versions 4.2.1 and earlier of `jsonwebtoken` are affected by a verification bypass vulnerability. This is a result of weak validation of the JWT algorithm type, occuring when an attacker is allowed to arbitrarily specify the JWT algorithm.\n\n\n\n\n## Recommendation\n\nUpdate to version 4.2.2 or later.\n\n ### References: \n- https://nvd.nist.gov/vuln/detail/CVE-2015-9235\n- https://github.com/auth0/node-jsonwebtoken/commit/1bb584bc382295eeb7ee8c4452a673a77a68b687\n- https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/\n- https://github.com/advisories/GHSA-c7hr-j4mj-j2w6\n- https://www.npmjs.com/advisories/17\n- https://www.timmclean.net/2015/02/25/jwt-alg-none.html",
    "source": "Dependabot",
    "severity": "CRITICAL",
    "armorcodeCategory": "Secrets",
    "findingCategory": "Vulnerability",
    "category": "Vulnerability",
    "status": "OPEN",
    "productStatus": "Active",
    "subProductStatuses": "Active",
    "id": 659573042,
    "tid": 161,
    "policy": null,
    "lastUpdated": 1717526668000,
    "createdAt": 1715361339000,
    "externalMappings": {},
    "title": "jsonwebtoken : = 0.4.0 - Verification Bypass in jsonwebtoken",
    "armorcodeTicket": [],
    "toolSeverity": "CRITICAL",
    "cwe": [
        "20"
    ],
    "cve": [
        "CVE-2015-9235"
    ],
    "product": {
        "id": 158036,
        "name": "PRODUCT_NAME"
    },
    "subProduct": {
        "id": 346991,
        "name": "SUBPRODUCT_NAME"
    },
    "environment": {
        "id": 679687,
        "name": "Production"
    },
    "securityOwner": {
        "id": null,
        "name": null
    },
    "owner": {
        "id": null,
        "name": null
    },
    "developer": "bjenkins-armorcode@gmail.com",
    "developerName": "Brian Jenkins",
    "toolId": "RVA_kwDOLpS_Gc8AAAABR2PYgQ",
    "filePath": "package.json",
    "url": "https://github.com/bjenkins-armorcode/juice-shop/security/dependabot/1",
    "lineNumber": null,
    "mitigated": false,
    "scan": 19280155,
    "scanType": [
        "SCA"
    ],
    "analysisType": "STATIC",
    "similarFindings": null,
    "additionalDetails": {
        "COMMIT_MESSAGE": "Import juice-shop",
        "FIXED_BY_DEVELOPER_EMAIL": "bjenkins-armorcode@gmail.com",
        "isCISAKEV": false,
        "FIXED_COMMIT_MESSAGE": "Import juice-shop",
        "cvssVectorV2": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
        "COMMIT_URL": "https://github.com/bjenkins-armorcode/juice-shop/commit/71513add1e6e56dc66395fdc7f405e7eb8953d31",
        "cvssVectorV3": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
        "epssScore": 0.75142,
        "repositoryName": "bjenkins-armorcode/juice-shop",
        "FIXED_COMMIT_URL": "https://github.com/bjenkins-armorcode/juice-shop/commit/71513add1e6e56dc66395fdc7f405e7eb8953d31",
        "componentFixVersions": "4.2.2",
        "repositoryUrl": "https://github.com/bjenkins-armorcode/juice-shop",
        "cveUsed": "CVE-2015-9235",
        "aeName": "Production",
        "exploited": false,
        "FIXED_BY_DEVELOPER_NAME": "Brian Jenkins",
        "dateSource": "tool",
        "scanType": "SCA",
        "toolFindingStatus": "OPEN",
        "category": "Vulnerability",
        "aatiScore": 8.04,
        "toolStatusOriginal": "OPEN",
        "cvePublishedDate": 1527625740000,
        "cveLastModifiedVulDate": 1570662900000
    },
    "slaBreached": true,
    "unsupressTime": null,
    "componentName": "jsonwebtoken",
    "componentVersion": "= 0.4.0",
    "slaDueDate": 1715019036000,
    "triageDueDate": 1714587036000,
    "remediationDueDate": null,
    "underReview": null,
    "proposedData": null,
    "tagsMetaMap": {
        "SUBPRODUCT": []
    },
    "team": {
        "id": null,
        "name": null
    },
    "tags": [],
    "foundOn": 1714414236000,
    "foundOnDate": 1714414236000,
    "baseScore": 9.8,
    "impactScore": 5.9,
    "exploitabilityScore": 3.9,
    "publishedDate": 1527625740000,
    "lastModifiedDate": 1570662900000,
    "issueResolved": null,
    "toolFindingStatus": "OPEN",
    "toolStatusOriginal": null,
    "cvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
    "newUrl": null,
    "findingScore": 5.1,
    "riskScore": null,
    "armorcodeProjects": null,
    "vendor": null,
    "subProductVersion": null,
    "productVersion": null,
    "mitigatedAt": null,
    "lastTriagedDate": null,
    "lastConfirmDate": null,
    "lastFalsePositiveDate": null,
    "lastOpenDate": 1715361339930,
    "lastAcceptRiskDate": null,
    "lastSuppressDate": null,
    "lastSeenDate": 1715299200000,
    "lastTriagedDateTime": null,
    "lastConfirmDateTime": null,
    "lastFalsePositiveDateTime": null,
    "lastOpenDateTime": 1715361339000,
    "lastAcceptRiskDateTime": null,
    "lastSuppressDateTime": null,
    "lastControlledDateTime": null,
    "lastInProgressDateTime": null,
    "lastTriageDateTime": null,
    "indirectExportFields": null,
    "assetScore": null,
    "comments": null,
    "history": null,
    "exploitMetaInfo": null,
    "attachments": null,
    "tagsUsedForAssetScore": [],
    "versionFindingsCount": null,
    "correlatedFindingsCount": null,
    "vmHostIpAddresses": null,
    "riskRegisters": null,
    "ctiScore": null,
    "cwesStrings": [
        "CWE-20"
    ],
    "assessment": []
}
```

</details>

<!--  -->

<details><summary><code>client.get_all_findings_by_saved_search_id(saved_search_id)</code></summary>

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
findings = await client.get_all_findings_by_saved_search_id(saved_search_id)
```
</td>
			<td>

```http
GET https://app.armorcode.com/user/findings/saved-search/{{saved_search_id}}
    ?page=0
    &size=100
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
            "ruleId": [
                "1.327",
                "1.20"
            ],
            "mitigation": "Patched version: 4.2.2",
            "impact": null,
            "stepsToReproduce": null,
            "description": "Versions 4.2.1 and earlier of `jsonwebtoken` are affected by a verification bypass vulnerability. This is a result of weak validation of the JWT algorithm type, occuring when an attacker is allowed to arbitrarily specify the JWT algorithm.\n\n\n\n\n## Recommendation\n\nUpdate to version 4.2.2 or later.\n\n ### References: \n- https://nvd.nist.gov/vuln/detail/CVE-2015-9235\n- https://github.com/auth0/node-jsonwebtoken/commit/1bb584bc382295eeb7ee8c4452a673a77a68b687\n- https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/\n- https://github.com/advisories/GHSA-c7hr-j4mj-j2w6\n- https://www.npmjs.com/advisories/17\n- https://www.timmclean.net/2015/02/25/jwt-alg-none.html",
            "source": "Dependabot",
            "severity": "CRITICAL",
            "armorcodeCategory": "Secrets",
            "findingCategory": "Vulnerability",
            "category": "Vulnerability",
            "status": "OPEN",
            "productStatus": "Active",
            "subProductStatuses": "Active",
            "id": 659573042,
            "tid": 161,
            "policy": null,
            "lastUpdated": 1717526668000,
            "createdAt": 1715361339000,
            "externalMappings": {},
            "title": "jsonwebtoken : = 0.4.0 - Verification Bypass in jsonwebtoken",
            "armorcodeTicket": [],
            "toolSeverity": "CRITICAL",
            "cwe": [
                "20"
            ],
            "cve": [
                "CVE-2015-9235"
            ],
            "product": {
                "id": 158036,
                "name": "PRODUCT_NAME"
            },
            "subProduct": {
                "id": 346991,
                "name": "SUBPRODUCT_NAME"
            },
            "environment": {
                "id": 679687,
                "name": "Production"
            },
            "securityOwner": {
                "id": null,
                "name": null
            },
            "owner": {
                "id": null,
                "name": null
            },
            "developer": "bjenkins-armorcode@gmail.com",
            "developerName": "Brian Jenkins",
            "toolId": "RVA_kwDOLpS_Gc8AAAABR2PYgQ",
            "filePath": "package.json",
            "url": "https://github.com/bjenkins-armorcode/juice-shop/security/dependabot/1",
            "lineNumber": null,
            "mitigated": false,
            "scan": 19280155,
            "scanType": [
                "SCA"
            ],
            "analysisType": "STATIC",
            "similarFindings": null,
            "additionalDetails": {
                "COMMIT_MESSAGE": "Import juice-shop",
                "FIXED_BY_DEVELOPER_EMAIL": "bjenkins-armorcode@gmail.com",
                "isCISAKEV": false,
                "FIXED_COMMIT_MESSAGE": "Import juice-shop",
                "cvssVectorV2": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                "COMMIT_URL": "https://github.com/bjenkins-armorcode/juice-shop/commit/71513add1e6e56dc66395fdc7f405e7eb8953d31",
                "cvssVectorV3": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                "epssScore": 0.75142,
                "repositoryName": "bjenkins-armorcode/juice-shop",
                "FIXED_COMMIT_URL": "https://github.com/bjenkins-armorcode/juice-shop/commit/71513add1e6e56dc66395fdc7f405e7eb8953d31",
                "componentFixVersions": "4.2.2",
                "repositoryUrl": "https://github.com/bjenkins-armorcode/juice-shop",
                "cveUsed": "CVE-2015-9235",
                "aeName": "Production",
                "exploited": false,
                "FIXED_BY_DEVELOPER_NAME": "Brian Jenkins",
                "dateSource": "tool",
                "scanType": "SCA",
                "toolFindingStatus": "OPEN",
                "category": "Vulnerability",
                "aatiScore": 8.04,
                "toolStatusOriginal": "OPEN",
                "cvePublishedDate": 1527625740000,
                "cveLastModifiedVulDate": 1570662900000
            },
            "slaBreached": true,
            "unsupressTime": null,
            "componentName": "jsonwebtoken",
            "componentVersion": "= 0.4.0",
            "slaDueDate": 1715019036000,
            "triageDueDate": 1714587036000,
            "remediationDueDate": null,
            "underReview": null,
            "proposedData": null,
            "tagsMetaMap": {
                "SUBPRODUCT": []
            },
            "team": {
                "id": null,
                "name": null
            },
            "tags": [],
            "foundOn": 1714414236000,
            "foundOnDate": 1714414236000,
            "baseScore": 9.8,
            "impactScore": 5.9,
            "exploitabilityScore": 3.9,
            "publishedDate": 1527625740000,
            "lastModifiedDate": 1570662900000,
            "issueResolved": null,
            "toolFindingStatus": "OPEN",
            "toolStatusOriginal": null,
            "cvssVector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
            "newUrl": null,
            "findingScore": 5.1,
            "riskScore": null,
            "armorcodeProjects": null,
            "vendor": null,
            "subProductVersion": null,
            "productVersion": null,
            "mitigatedAt": null,
            "lastTriagedDate": null,
            "lastConfirmDate": null,
            "lastFalsePositiveDate": null,
            "lastOpenDate": 1715361339930,
            "lastAcceptRiskDate": null,
            "lastSuppressDate": null,
            "lastSeenDate": 1715299200000,
            "lastTriagedDateTime": null,
            "lastConfirmDateTime": null,
            "lastFalsePositiveDateTime": null,
            "lastOpenDateTime": 1715361339000,
            "lastAcceptRiskDateTime": null,
            "lastSuppressDateTime": null,
            "lastControlledDateTime": null,
            "lastInProgressDateTime": null,
            "lastTriageDateTime": null,
            "indirectExportFields": null,
            "assetScore": null,
            "comments": null,
            "history": null,
            "exploitMetaInfo": null,
            "attachments": null,
            "tagsUsedForAssetScore": [],
            "versionFindingsCount": null,
            "correlatedFindingsCount": null,
            "vmHostIpAddresses": null,
            "riskRegisters": null,
            "ctiScore": null,
            "cwesStrings": [
                "CWE-20"
            ],
            "assessment": []
        }
    ],
    "pageable": {
        "pageNumber": 0,
        "pageSize": 100,
        "sort": {
            "sorted": true,
            "empty": false,
            "unsorted": false
        },
        "offset": 0,
        "paged": true,
        "unpaged": false
    },
    "last": false,
    "totalElements": 1,
    "totalPages": 1,
    "first": true,
    "size": 100,
    "number": 0,
    "sort": {
        "sorted": true,
        "empty": false,
        "unsorted": false
    },
    "numberOfElements": 1,
    "empty": false
}
```

</details>


`client.update_finding_by_id()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

### Integrations

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

`client.create_configuration()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.update_configuration_by_id()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.delete_configuration_by_id()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

### Security Tools

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

### Logins

<details><summary><code>client.get_all_logins_by_tool_name(tool_name)</code></summary>

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


`client.create_login()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

### Products

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


`client.create_product()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.update_product_by_id()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.delete_product_by_id()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

### Sub-products

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


`client.create_subproduct()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.update_subproduct_by_id()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.delete_subproduct_by_id()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

### Teams

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

`client.create_team()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.update_team_by_id(team_id)` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.delete_team_by_id(team_id)` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

### Users

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

`client.create_user()` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.update_user_by_id(user_id)` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

`client.delete_user_by_id(user_id)` <sup><sup>NOT YET IMPLEMENTED</sup></sup>

## Advanced Usage

If you have calls that you would like to make that the SDK does not give you the desired customizability over, you can use the underlying [`fetch`](/acsdk/util/fetch_without_logging.py) function to ensure that your requests adhere to ArmorCode's API request limit.

> [!WARNING]
> Depending on the API call, you may have to handle pagination yourself.

```python
import asyncio
from acsdk import ArmorCodeClient, fetch

async def main(api_key):
    client = ArmorCodeClient(api_key)

    page_number = None

    products = await fetch(client, "get", "/user/product/elastic/paged", params=list({
        "environmentName": "PRODUCTION",
        "pageSize": "100",
        **({"pageNumber": str(page_number)} if page_number is not None else {}),
        "tags": "",
        "sortBy": "NAME",
        "direction": "ASC"
    }.items()))

    print(products)

    await client.close()
```
