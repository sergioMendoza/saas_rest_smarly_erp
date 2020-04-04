from django.db import models
from tenant_schemas.models import TenantMixin

# Utilities
from saas_smarly_erp.utils.models import SmarlyModel


class Client(SmarlyModel, TenantMixin):
    """
    TenantMixin has 2 fields
        - domain_url
        - schema_name
    """
    tenant_id = models.CharField(max_length=255)
    company_name = models.CharField(max_length=250)
    account_name = models.CharField(max_length=250)
    owner_name = models.CharField(max_length=250)
    tier = models.CharField(max_length=100)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
