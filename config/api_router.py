from django.conf import settings
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('saas_smarly_erp.apps.customers.urls')),
    path('', include('saas_smarly_erp.apps.users.urls'))
]
