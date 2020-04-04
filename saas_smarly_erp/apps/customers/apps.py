from django.apps import AppConfig


class CustomersConfig(AppConfig):
    name = 'customers'

    def ready(self):
        try:
            import saas_smarly_erp.apps.customers.signals  # noqa F401
        except ImportError:
            pass
