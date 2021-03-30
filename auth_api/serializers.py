from rest_framework import serializers
from .models import User, Vendor, DeviceOwner


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        exclude = ('password','groups','user_permissions')


class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor


class DeviceOwnerSerializer(serializers.Serializer):
    class Meta:
        model = DeviceOwner