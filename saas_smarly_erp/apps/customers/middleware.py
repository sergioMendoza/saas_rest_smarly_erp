"""Middleware to extract tenant from header request"""

# tenant-schema
from tenant_schemas.middleware import BaseTenantMiddleware, get_public_schema_name


class XHeaderTenantMiddleware(BaseTenantMiddleware):
    """
    Determinate tenant by the value of the ``X-DTS-SCHEMA`` HTTP header
    """

    def get_tenant(self, model, hostname, request):
        schema_name = request.META.get('HTTP_X_DTS_SCHEMA', get_public_schema_name())
        return model.objects.get(schema_name=schema_name)
