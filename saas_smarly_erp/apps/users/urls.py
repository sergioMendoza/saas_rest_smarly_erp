"""Users URLs"""

# Django
from django.urls import path, include

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from saas_smarly_erp.apps.users.views import (
    UserModelViewSet,
)

router = DefaultRouter()
router.register(r'users', UserModelViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls)),
]
