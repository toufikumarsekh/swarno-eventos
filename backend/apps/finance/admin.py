from django.contrib import admin
from .models import Payment, Expense


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "receipt_number", "company", "client",
        "payment_type", "amount", "payment_date",
        "method", "status",
    )
    list_filter = ("status", "payment_type", "method", "payment_date")
    search_fields = ("receipt_number", "client__name", "transaction_reference")
    readonly_fields = (
        "receipt_number", "posted_at", "voided_at",
        "created_at", "updated_at",
    )
    list_select_related = ("company", "client", "event", "quotation")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "expense_number", "company", "title",
        "category", "payee", "amount", "expense_date", "status",
    )
    list_filter = ("status", "category", "method", "expense_date")
    search_fields = (
        "expense_number", "title", "payee", "transaction_reference",
    )
    readonly_fields = (
        "expense_number", "posted_at", "voided_at",
        "created_at", "updated_at",
    )
    list_select_related = ("company", "event")
