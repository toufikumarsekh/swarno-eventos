from django.urls import path
from . import views

app_name = "finance"

urlpatterns = [
    path("", views.finance_dashboard, name="dashboard"),

    path("payments/", views.payment_list, name="payments"),
    path("payments/new/", views.payment_create, name="payment_create"),
    path("payments/<int:pk>/", views.payment_detail, name="payment_detail"),
    path("payments/<int:pk>/void/", views.payment_void, name="payment_void"),

    path("expenses/", views.expense_list, name="expenses"),
    path("expenses/new/", views.expense_create, name="expense_create"),
    path("expenses/<int:pk>/", views.expense_detail, name="expense_detail"),
    path("expenses/<int:pk>/void/", views.expense_void, name="expense_void"),
]
