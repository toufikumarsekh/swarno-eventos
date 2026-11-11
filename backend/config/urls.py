from django.contrib import admin
from django.urls import path, include
from apps.core.views import home, health_check

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("companies/", include("apps.companies.urls")),
    path("api/health/", health_check, name="health"),
]
