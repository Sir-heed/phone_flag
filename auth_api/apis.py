from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout, authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, VendorSerializer, DeviceOwnerSerializer, LoginSerializer
from .models import User, Vendor, DeviceOwner

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'code': 200,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user': request.user.email
                        }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "code": 110,
                        "message": "inactive user",
                        "resolve": "proceed to activate your account"
                    }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                    return Response({
                        "code": 120,
                        "message": "invalid crendetials",
                        "resolve": "There's no account matching this email and password"
                    }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)