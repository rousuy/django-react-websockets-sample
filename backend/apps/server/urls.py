from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.server import views

router = DefaultRouter()

router.register(
    "select",
    views.ServerViewSet,
    basename="servers",
)

urlpatterns = [path("", include(router.urls))]
