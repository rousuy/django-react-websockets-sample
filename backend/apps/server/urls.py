from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.server import views

router = DefaultRouter()

router.register(
    "servers/categories",
    views.CategoryViewSet,
    basename="categories",
)

router.register(
    "servers/channels",
    views.ChannelViewSet,
    basename="channels",
)

router.register(
    "servers",
    views.ServerViewSet,
    basename="servers",
)

urlpatterns = [path("", include(router.urls))]
