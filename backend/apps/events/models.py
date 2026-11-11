from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from apps.companies.models import Company
from apps.clients.models import Client
from apps.enquiries.models import Enquiry


class Event(models.Model):

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        CONFIRMED = "confirmed", "Confirmed"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    class EventType(models.TextChoices):
        WEDDING = "wedding", "Wedding"
        BIRTHDAY = "birthday", "Birthday"
        CORPORATE = "corporate", "Corporate"
        CONCERT = "concert", "Concert"
        COLLEGE = "college", "College Fest"
        EXHIBITION = "exhibition", "Exhibition"
        CULTURAL = "cultural", "Cultural Event"
        OTHER = "other", "Other"

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="events"
    )
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, related_name="events"
    )
    enquiry = models.ForeignKey(
        Enquiry, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="events"
    )

    title = models.CharField(max_length=200)
    event_type = models.CharField(
        max_length=30, choices=EventType.choices, default=EventType.OTHER
    )
    event_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=250, blank=True)
    guest_count = models.PositiveIntegerField(default=0)
    budget = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_events",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_date", "start_time"]
        indexes = [
            models.Index(fields=["company", "event_date"]),
            models.Index(fields=["company", "status"]),
        ]

    def clean(self):
        super().clean()

        if self.client_id and self.company_id:
            if self.client.company_id != self.company_id:
                raise ValidationError(
                    {"client": "Client must belong to this company."}
                )

        if self.enquiry_id and self.company_id:
            if self.enquiry.company_id != self.company_id:
                raise ValidationError(
                    {"enquiry": "Enquiry must belong to this company."}
                )
            if self.client_id and self.enquiry.client_id != self.client_id:
                raise ValidationError(
                    {"enquiry": "Enquiry must belong to the selected client."}
                )

        if self.start_time and self.end_time:
            if self.end_time <= self.start_time:
                raise ValidationError(
                    {"end_time": "End time must be later than start time."}
                )

    def __str__(self):
        return self.title
