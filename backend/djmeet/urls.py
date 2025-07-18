from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("api/", include("apps.account.urls"), name="accounts"),
    path("api/", include("apps.server.urls"), name="servers"),
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/schema/ui/", SpectacularSwaggerView.as_view()),
]

if settings.DEBUG:
    urlpatterns.append(path("silk/", include("silk.urls"), name="silk"))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
