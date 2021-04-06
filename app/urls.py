from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .apis import DeviceViewSet

router = DefaultRouter()
router.register('device', DeviceViewSet, 'device')

urlpatterns = router.urls
urlpatterns += [
]