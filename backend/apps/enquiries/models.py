from django.conf import settings
from django.db import models


class Enquiry(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        QUALIFIED = "qualified", "Qualified"
        PROPOSAL = "proposal", "Proposal Sent"
        CONVERTED = "converted", "Converted"
        LOST = "lost", "Lost"

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="enquiries",
    )
    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.PROTECT,
        related_name="enquiries",
    )
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=100)
    event_date = models.DateField(null=True, blank=True)
    guest_count = models.PositiveIntegerField(default=0)
    venue = models.CharField(max_length=250, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    source = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_enquiries",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["company", "status"]),
            models.Index(fields=["company", "event_date"]),
        ]

    def __str__(self):
        return self.title


class FollowUp(models.Model):
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="enquiry_followups",
    )
    enquiry = models.ForeignKey(
        Enquiry,
        on_delete=models.CASCADE,
        related_name="followups",
    )
    scheduled_at = models.DateTimeField()
    note = models.TextField()
    outcome = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_followups",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["is_completed", "scheduled_at"]

    def __str__(self):
        return f"Follow-up: {self.enquiry.title}"
