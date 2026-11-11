from django.contrib import admin
from .models import Quotation, QuotationItem


class QuotationItemInline(admin.TabularInline):
    model = QuotationItem
    extra = 0


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        "number", "title", "company", "client",
        "status", "issue_date", "version",
    )
    list_filter = ("status", "issue_date", "company")
    search_fields = ("number", "title", "client__name")
    inlines = [QuotationItemInline]


@admin.register(QuotationItem)
class QuotationItemAdmin(admin.ModelAdmin):
    list_display = ("description", "quotation", "quantity", "unit_price")
