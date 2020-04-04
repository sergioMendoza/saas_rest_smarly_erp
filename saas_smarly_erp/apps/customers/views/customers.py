"""Customers Views"""

import logging
from requests.exceptions import RequestException
# Django REST Framework
from rest_framework import (
    status,
    viewsets,
    mixins,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# Tenant
from tenant_schemas.utils import tenant_context

# Serializers
from saas_smarly_erp.apps.customers.serializers.customers import (
    CustomerModelSerializer
)
from saas_smarly_erp.apps.users.serializers import (
    UserSignUpSerializer
)

# Models
from saas_smarly_erp.apps.customers.models import Client

# Services
from saas_smarly_erp.apps.cognito.services import TenantService

# Utils
from saas_smarly_erp.utils.tenant import (
    generate_schema_name,
    get_tenant_domain_url
)

logger = logging.getLogger(__name__)


class CustomerViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Customer API view"""

    queryset = Client.objects.all()
    serializer_class = CustomerModelSerializer
    permission_classes = []
    lookup_field = 'schema_name'

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Customer sign up and user create"""

        if request.data.get('user') is None:
            return Response({'user': ["This field is required"]}, status=status.HTTP_400_BAD_REQUEST)

        user_data = request.data.pop('user')

        customer_serializer = CustomerModelSerializer(data=request.data)
        customer_serializer.is_valid(raise_exception=True)

        user_serializer = UserSignUpSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        try:

            tenant_data = {'companyName': customer_serializer.validated_data['company_name'],
                           'accountName': customer_serializer.validated_data['account_name'],
                           'ownerName': customer_serializer.validated_data['owner_name'],
                           'tier': customer_serializer.validated_data['tier'],
                           'email': user_serializer.validated_data['email'],
                           'userName': user_serializer.validated_data['username'],
                           'firstName': user_serializer.validated_data['first_name'],
                           'lastName': user_serializer.validated_data['last_name']}

            tenant_service = TenantService.register_tenant(tenant_data)
            schema_name = generate_schema_name(tenant_data['companyName'])
            domain_url = get_tenant_domain_url(schema_name)
            tenant_id = tenant_service['tenant_id']

            logger.warning('--------------------------------------')
            logger.info(tenant_service)
            logger.info(schema_name)
            logger.info(domain_url)
            logger.info(tenant_id)
            logger.warning('--------------------------------------')

            customer = customer_serializer.save(domain_url=domain_url, schema_name=schema_name, tenant_id=tenant_id)

            with tenant_context(customer):
                """Save user in customers schema"""
                user = user_serializer.save()

                customer = CustomerModelSerializer(customer).data
                user = UserSignUpSerializer(user).data
                customer['user'] = user

                data = {
                    'customer': customer
                }

                return Response(data, status=status.HTTP_201_CREATED)

        except RequestException:
            return Response({}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
