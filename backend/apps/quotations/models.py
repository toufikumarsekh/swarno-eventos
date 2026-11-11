from decimal import Decimal, ROUND_HALF_UP

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from apps.companies.models import Company
from apps.clients.models import Client
from apps.events.models import Event


class Quotation(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SENT = "sent", "Sent"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"
        EXPIRED = "expired", "Expired"

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="quotations"
    )
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, related_name="quotations"
    )
    event = models.ForeignKey(
        Event, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="quotations"
    )

    number = models.CharField(max_length=40, null=True, blank=True)
    version = models.PositiveIntegerField(default=1)

    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    issue_date = models.DateField(default=timezone.localdate)
    valid_until = models.DateField(null=True, blank=True)

    terms_and_conditions = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="created_quotations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["company", "number", "version"],
                name="unique_company_quotation_version",
            )
        ]
        indexes = [
            models.Index(fields=["company", "status"]),
            models.Index(fields=["company", "issue_date"]),
        ]

    def save(self, *args, **kwargs):
        if not self.number and self.pk is None:
            super().save(*args, **kwargs)
            self.number = f"QTN-{timezone.localdate().year}-{self.pk:05d}"
            super().save(update_fields=["number"])
            return
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.client_id and self.company_id:
            if self.client.company_id != self.company_id:
                raise ValidationError(
                    {"client": "Client must belong to this company."}
                )
        if self.event_id and self.company_id:
            if self.event.company_id != self.company_id:
                raise ValidationError(
                    {"event": "Event must belong to this company."}
                )
            if self.client_id and self.event.client_id != self.client_id:
                raise ValidationError(
                    {"event": "Event must belong to the selected client."}
                )
        if self.valid_until and self.issue_date:
            if self.valid_until < self.issue_date:
                raise ValidationError(
                    {"valid_until": "Validity date cannot be before issue date."}
                )

    @property
    def subtotal(self):
        return sum(
            (item.base_amount for item in self.items.all()),
            Decimal("0.00"),
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @property
    def discount_total(self):
        return sum(
            (item.discount_amount for item in self.items.all()),
            Decimal("0.00"),
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @property
    def tax_total(self):
        return sum(
            (item.tax_amount for item in self.items.all()),
            Decimal("0.00"),
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @property
    def grand_total(self):
        return (self.subtotal - self.discount_total + self.tax_total).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    def __str__(self):
        return self.number or self.title


class QuotationItem(models.Model):
    quotation = models.ForeignKey(
        Quotation, on_delete=models.CASCADE, related_name="items"
    )
    description = models.CharField(max_length=250)
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("1.00")
    )
    unit = models.CharField(max_length=30, default="Unit", blank=True)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    discount_percent = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )
    tax_percent = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )

    class Meta:
        ordering = ["id"]

    def clean(self):
        super().clean()

        if self.quantity is not None and self.quantity <= 0:
            raise ValidationError({"quantity": "Quantity must be greater than zero."})

        if self.unit_price is not None and self.unit_price < 0:
            raise ValidationError({"unit_price": "Unit price cannot be negative."})

        if self.discount_percent is not None:
            if not Decimal("0") <= self.discount_percent <= Decimal("100"):
                raise ValidationError({
                    "discount_percent": "Discount must be between 0 and 100."
                })

        if self.tax_percent is not None:
            if not Decimal("0") <= self.tax_percent <= Decimal("100"):
                raise ValidationError({
                    "tax_percent": "Tax must be between 0 and 100."
                })

    @property
    def base_amount(self):
        return (self.quantity * self.unit_price).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    @property
    def discount_amount(self):
        return (self.base_amount * self.discount_percent / Decimal("100")).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    @property
    def taxable_amount(self):
        return self.base_amount - self.discount_amount

    @property
    def tax_amount(self):
        return (self.taxable_amount * self.tax_percent / Decimal("100")).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    @property
    def total_amount(self):
        return self.taxable_amount + self.tax_amount

    def __str__(self):
        return self.description
