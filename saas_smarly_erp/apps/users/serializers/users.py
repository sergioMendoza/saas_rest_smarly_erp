"""User Serializer"""

# Django
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator

# Django REST
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from saas_smarly_erp.apps.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta class"""

        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number'
        )

    def create(self, validated_data):
        """Create a Super User with set_unusable_password """


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer

    Handle sign up data validation and user creation
    """
    email = serializers.EmailField()

    username = serializers.CharField(
        min_length=4,
        max_length=100,

    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format +999999999. Up to 15 digits allowed.'
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_unusable_password()
        user.save()
        return user
