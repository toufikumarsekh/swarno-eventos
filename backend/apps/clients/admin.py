from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "phone", "email", "created_at")
    list_filter = ("company",)
    search_fields = ("name", "phone", "email")
    readonly_fields = ("created_at", "updated_at")
