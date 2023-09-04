from django.urls import include, path
from rest_framework.routers import DefaultRouter
from server.views.server import ServerViewSet

router = DefaultRouter()

router.register(
    "select",
    ServerViewSet,
    basename="servers",
)

urlpatterns = [path("", include(router.urls))]
