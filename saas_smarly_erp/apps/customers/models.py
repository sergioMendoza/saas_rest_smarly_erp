from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    """
    TenantMixin has 2 fields
        - domain_url
        - schema_name
    """
    name = models.CharField(max_length=100)
    tenant_id = models.CharField(max_length=255)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
