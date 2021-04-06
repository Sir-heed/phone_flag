from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .apis import LoginView, DeviceOwnerSignUpViewSet, VendorSignUpViewSet

router = DefaultRouter()
router.register('vendor', VendorSignUpViewSet, 'vendor')
router.register('device_owner', DeviceOwnerSignUpViewSet, 'device_owner')

urlpatterns = router.urls
urlpatterns += [
    path('login/', LoginView.as_view(), name='login'),
]