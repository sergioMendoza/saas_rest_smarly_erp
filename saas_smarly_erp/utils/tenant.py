"""Tenant Utils"""
from django.conf import settings


def get_tenant_domain_url(schema_name):
    main_domain = getattr(settings, "MAIN_DOMAIN_URL", settings.MAIN_DOMAIN_URL)
    return "%s.%s" % (schema_name, main_domain)


def generate_schema_name(company_name):
    schema_name = company_name.replace(" ", "").lower()
    return schema_name
