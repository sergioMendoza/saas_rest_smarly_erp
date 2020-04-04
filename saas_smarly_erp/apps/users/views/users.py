"""Users Views"""

# Django REST Framework
from rest_framework import (
    status,
    viewsets,

)
from rest_framework.permissions import IsAuthenticated

# Serializers
from saas_smarly_erp.apps.users.serializers.users import (
    UserModelSerializer
)

# Models
from saas_smarly_erp.apps.users.models import User


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer()
    permission_classes = [IsAuthenticated]
