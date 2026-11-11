from django.urls import path, include
from . import views

app_name = "companies"

urlpatterns = [
    path("", views.company_list, name="list"),
    path("register/", views.register_company, name="register"),
    path("success/", views.registration_success, name="success"),
    path("<slug:slug>/dashboard/", views.company_dashboard, name="dashboard"),

    path(
        "<slug:company_slug>/clients/",
        include("apps.clients.urls", namespace="clients"),
    ),
    path(
        "<slug:company_slug>/enquiries/",
        include("apps.enquiries.urls", namespace="enquiries"),
    ),
    path(
        "<slug:company_slug>/quotations/",
        include("apps.quotations.urls", namespace="quotations"),
    ),

    path(
        "<slug:company_slug>/finance/",
        include("apps.finance.urls", namespace="finance"),
    ),

    path(
        "<slug:company_slug>/events/",
        include("apps.events.urls", namespace="events"),
    ),
]
