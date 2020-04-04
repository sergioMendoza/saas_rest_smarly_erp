import os

from django.apps import AppConfig, apps
from django.conf import settings

from celery import Celery  # , signals
from celery.schedules import crontab

if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover

from tenant_schemas_celery.app import CeleryApp



app = Celery('saas_smarly_erp')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
if os.environ.get('DJANGO_SETTINGS_MODULE', None) == 'config.settings.local':

    app.config_from_object('django.conf:settings', namespace='CELERY')
else:
    app.config_from_object('django.conf:settings')


class CeleryAppConfig(AppConfig):
    name = 'saas_smarly_erp.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)

        if hasattr(settings, 'RAVEN_CONFIG'):
            # Celery signal registration

            from raven import Client as RavenClient
            from raven.contrib.celery import register_signal as raven_register_signal  # noqa:E501
            from raven.contrib.celery import register_logger_signal as raven_register_logger_signal  # noqa:E501

            raven_client = RavenClient(dsn=settings.RAVEN_CONFIG['dsn'])
            raven_register_logger_signal(raven_client)
            raven_register_signal(raven_client)
