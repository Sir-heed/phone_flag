from rest_framework import serializers
from .models import User, Vendor, DeviceOwner


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['last_login', 'active', 'staff', 'admin']


class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Vendor
        # fields = '__all__'
        exclude = ['id']


class DeviceOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = DeviceOwner
        # fields = '__all__'
        exclude = ['id']