import aiohttp
import re

from .version import __version__

class ArmorCodeClient(aiohttp.ClientSession):
    version = __version__

    def __init__(self, api_key, overrides={}):
        if not re.search(r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", api_key):
            raise TypeError("This doesn't look like any API key that I've ever seen!")

        connector = aiohttp.TCPConnector()

        super().__init__(base_url=overrides.get("base_url", "https://app.armorcode.com"), connector=connector, headers={
            "Authorization": "Bearer " + api_key,
            "User-Agent": "ArmorCode Python SDK v" + __version__
        })


    # ===== from .alerts import * =====

    from .alerts import _get_all_alerts

    def get_all_alerts(self):
        return self._get_all_alerts()


    # ===== from .findings import * =====

    from .findings import _get_all_findings

    def get_all_findings(self):
        return self._get_all_findings()


    from .findings import _get_finding_by_id

    def get_finding_by_id(self, finding_id):
        return self._get_finding_by_id(finding_id)


    from .findings import _get_all_findings_by_saved_search_id

    def get_all_findings_by_saved_search_id(self, saved_search_id):
        return self._get_all_findings_by_saved_search_id(saved_search_id)


    # ===== from .installations import * =====

    from .installations import _get_all_installations_by_tool_name

    def get_all_installations_by_tool_name(self, tool_name):
        return self._get_all_installations_by_tool_name(tool_name)


    # ===== from .integrations import * =====

    from .integrations import _get_all_integrations

    def get_all_integrations(self):
        return self._get_all_integrations()


    from .integrations import _create_configuration

    # FIXME: Too many parameters.
    def create_configuration(self, configuration_name, configuration_token, configuration_host_url, configuration_repository_type):
        return self._create_configuration(configuration_name, configuration_token, configuration_host_url, configuration_repository_type)


    from .integrations import _delete_configuration_by_id

    def delete_configuration_by_id(self, configuration_id):
        return self._delete_configuration_by_id(configuration_id)


    # ===== from .logins import * =====

    from .logins import _get_all_mappings_by_login_id

    def get_all_mappings_by_login_id(self, tool_name, login_id):
        return self._get_all_mappings_by_login_id(tool_name, login_id)


    from .logins import _get_all_logins_by_tool_name

    def get_all_logins_by_tool_name(self, tool_name):
        return self._get_all_logins_by_tool_name(tool_name)


    from .logins import _get_all_projects_by_login_id

    def get_all_projects_by_login_id(self, tool_name, login_id):
        return self._get_all_projects_by_login_id(tool_name, login_id)


    from .logins import _get_project_by_name

    def get_project_by_name(self, tool_name, login_id, project_name):
        return self._get_project_by_name(tool_name, login_id, project_name)


    from .logins import _get_all_unmapped_projects_by_login_id

    def get_all_unmapped_projects_by_login_id(self, tool_name, login_id):
        return self._get_all_unmapped_projects_by_login_id(tool_name, login_id)


    from .logins import _create_login

    def create_login(self, tool_name):
        return self._create_login(tool_name)


    # ===== from .products import * =====

    from .products import _get_all_products

    def get_all_products(self):
        return self._get_all_products()


    from .products import _get_product_by_id

    def get_product_by_id(self, product_id):
        return self._get_product_by_id(product_id)


    from .products import _get_products_by_name

    def get_products_by_name(self, product_name):
        return self._get_products_by_name(product_name)


    from .products import _update_product_by_id

    def update_product_by_id(self, product_id, partial_product_payload):
        return self._update_product_by_id(product_id, partial_product_payload)


    from .products import _create_product

    def create_product(self, product_name, product_payload={}):
        return self._create_product(product_name, product_payload)


    from .products import _delete_product_by_id

    def delete_product_by_id(self, product_id):
        return self._delete_product_by_id(product_id)


    # ===== from .security_tools import * =====

    from .security_tools import _get_all_security_tools

    def get_all_security_tools(self):
        return self._get_all_security_tools()

    # ===== from .subproducts import * =====

    from .subproducts import _get_all_subproducts

    def get_all_subproducts(self):
        return self._get_all_subproducts()


    from .subproducts import _get_subproduct_by_id

    def get_subproduct_by_id(self, subproduct_id):
        return self._get_subproduct_by_id(subproduct_id)


    from .subproducts import _get_subproducts_by_name

    def get_subproducts_by_name(self, subproduct_name):
        return self._get_subproducts_by_name(subproduct_name)


    from .subproducts import _update_subproduct_by_id

    def update_subproduct_by_id(self, subproduct_id, partial_subproduct_payload={}):
        return self._update_subproduct_by_id(subproduct_id, partial_subproduct_payload)


    from .subproducts import _create_subproduct

    def create_subproduct(self, product_id, subproduct_name, subproduct_payload={}):
        return self._create_subproduct(product_id, subproduct_name, subproduct_payload)


    from .subproducts import _delete_subproduct_by_id

    def delete_subproduct_by_id(self, subproduct_id):
        return self._delete_subproduct_by_id(subproduct_id)


    # ===== from .teams import * =====

    from .teams import _get_all_teams

    def get_all_teams(self):
        return self._get_all_teams()

    # ===== from .users import * =====

    from .users import _get_all_users

    def get_all_users(self):
        return self._get_all_users()
