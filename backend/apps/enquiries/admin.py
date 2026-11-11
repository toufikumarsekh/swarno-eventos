from django.contrib import admin
from .models import Enquiry, FollowUp


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "client", "event_type", "event_date", "status")
    list_filter = ("company", "status", "event_type")
    search_fields = ("title", "client__name", "client__phone")
    readonly_fields = ("created_at", "updated_at")


@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):
    list_display = ("enquiry", "company", "scheduled_at", "is_completed")
    list_filter = ("company", "is_completed")
    readonly_fields = ("created_at",)
