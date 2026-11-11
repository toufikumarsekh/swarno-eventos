from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title", "company", "client", "event_date", "status"
    )
    list_filter = ("company", "status", "event_type", "event_date")
    search_fields = ("title", "client__name", "venue")
    readonly_fields = ("created_at", "updated_at")
