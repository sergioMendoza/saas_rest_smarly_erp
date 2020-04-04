"""Services to create tenant, user pool, user client in cognito AWS"""

import logging
import requests
import json
from django.conf import settings

logger = logging.getLogger(__name__)


class TenantService:

    @staticmethod
    def register_tenant(tenant_data):
        request_data = json.dumps(tenant_data)
        response = requests.post('https://dev-api.smarlyerp.com/tenants/reg', data=request_data)
        response.raise_for_status()
        json_data = response.json()
        return json_data

    def list_tenant_system(self):
        pass

    def list_tenant(self):
        pass

    def update_tenant(self):
        pass

    def delete_tenant(self):
        pass
