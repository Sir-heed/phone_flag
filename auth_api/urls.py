from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .apis import LoginView

router = DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path('login/', LoginView.as_view(), name='login'),
]