from tenant_schemas.signals import post_schema_sync
from tenant_schemas.models import TenantMixin

# Model
from saas_smarly_erp.apps.users.models import User


def create_customer_user(sender, tenant, **kwargs):
    """create user after the tenant is saved, its schema created and synced."""


post_schema_sync.connect(create_customer_user, sender=TenantMixin)
