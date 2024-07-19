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

`client.get_all_alerts()`

### Findings

`client.get_all_findings()`

`client.get_finding_by_id(finding_id)`

`client.get_all_findings_by_saved_search_id(saved_search_id)`

### Integrations

`client.get_all_integrations()`

### Security Tools

`client.get_all_security_tools()`

### Logins

`client.get_all_mappings_by_login_id(tool_name, login_id)`

`client.get_all_logins_by_tool_name(tool_name)`

`client.get_all_projects_by_login_id(tool_name, login_id)`

`client.get_project_by_name(tool_name, login_id, project_name)`

<!-- `client.create_login` -->

### Products

`client.get_all_products()`

`client.get_product_by_id(product_id)`

`client.get_products_by_name(product_name)`

<!-- `client.update_product_by_id` -->

<!-- `client.create_product` -->

<!-- `client.delete_product_by_id` -->

### Sub-products

`client.get_all_subproducts()`

`client.get_subproduct_by_id(subproduct_id)`

`client.get_subproducts_by_name(subproduct_name)`

<!-- `client.update_subproduct_by_id` -->

<!-- `client.create_subproduct` -->

<!-- `client.delete_subproduct_by_id` -->

### Teams

`client.get_all_teams()`

### Users

`client.get_all_users()`

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

## Common Workflows

### Update a sub-product with a tag

<table>
  <tbody>
    <tr>
        <td colspan="2" width="50%"><strong>Get all products</strong></td>
    </tr>
    <tr>
      <td width="50%">

```python
products = await client.get_all_products()
```
</td>
      <td width="50%">

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
    <tr>
        <td colspan="2" width="50%"><strong>Identify the product(s) you are interested in updating</strong></td>
    </tr>
    <tr>
      <td width="50%">

```python
product = list(
    filter(
        lambda product: product["name"].casefold() == product_name.casefold(), products
    )
)
```
</td>
      <td width="50%">

```http
```
</td>
    </tr>
  </tbody>
</table>