"""Users URLs"""

# Django
from django.urls import path, include

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from saas_smarly_erp.apps.customers.views import (
    CustomerViewSet,
)

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = [
    path('', include(router.urls)),
]
