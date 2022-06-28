from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from auth.urls import auth_router
from core.urls import core_router
from user.views import UserViewSet

router = DefaultRouter()
router.registry.extend(auth_router.registry)
router.registry.extend(core_router.registry)
router.register(r'user', UserViewSet, basename='user')

schema_view = get_schema_view(openapi.Info(title="Gym Log API", default_version='v1'), public=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include((router.urls, 'api'))),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Production frontend static files served from root path.
    re_path(".*", TemplateView.as_view(template_name="index.html")),
]
