from django.contrib import admin
from .models import Company, Membership


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "city", "is_active", "created_at")
    search_fields = ("name", "legal_name", "email", "phone", "slug")
    list_filter = ("is_active", "country", "state")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "role", "is_active", "joined_at")
    search_fields = ("user__email", "company__name")
    list_filter = ("role", "is_active", "company")
    readonly_fields = ("joined_at",)
