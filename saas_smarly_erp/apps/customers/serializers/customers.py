"""Customer Serializer"""

# Core
import logging

# Django REST
from rest_framework import serializers

# Model
from saas_smarly_erp.apps.customers.models import Client


logger = logging.getLogger(__name__)


class CustomerModelSerializer(serializers.ModelSerializer):
    """Customer model serializer"""

    class Meta:
        model = Client
        fields = [
            'company_name',
            'account_name',
            'owner_name',
            'tier',
        ]

    def create(self, validated_data):
        logger.info(validated_data)
        customer = Client.objects.create(**validated_data)
        return customer

