from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'ntel', 'role', 'date_naissance']


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'ntel', 'role', 'date_naissance', 'last_update_profile']
        read_only_fields = ['last_update_profile']
        #fields = '__all__'


class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email','is_active', 'date_joined', 'ntel', 'date_naissance']



# serializers.py
from djoser.serializers import UserCreateSerializer
from .utils import send_admin_email

class CustomUserCreateSerializer(UserCreateSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        send_admin_email(user)
        return user


class contactusSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    sender_email = serializers.EmailField()