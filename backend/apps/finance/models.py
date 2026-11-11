from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Payment(models.Model):

    class PaymentType(models.TextChoices):
        ADVANCE = "advance", "Advance"
        PARTIAL = "partial", "Partial Payment"
        FINAL = "final", "Final Payment"
        OTHER = "other", "Other"

    class Method(models.TextChoices):
        CASH = "cash", "Cash"
        UPI = "upi", "UPI"
        BANK = "bank", "Bank Transfer"
        CARD = "card", "Card"
        CHEQUE = "cheque", "Cheque"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        POSTED = "posted", "Posted"
        VOID = "void", "Void"

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="payments",
    )
    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.PROTECT,
        related_name="payments",
    )
    event = models.ForeignKey(
        "events.Event",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments",
    )
    quotation = models.ForeignKey(
        "quotations.Quotation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments",
    )

    receipt_number = models.CharField(max_length=40, null=True, blank=True)
    payment_type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
        default=PaymentType.ADVANCE,
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    payment_date = models.DateField(default=timezone.localdate)
    method = models.CharField(
        max_length=20,
        choices=Method.choices,
        default=Method.CASH,
    )
    transaction_reference = models.CharField(max_length=150, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    notes = models.TextField(blank=True)
    void_reason = models.TextField(blank=True)
    posted_at = models.DateTimeField(null=True, blank=True)
    voided_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_payments",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-payment_date", "-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["company", "receipt_number"],
                name="unique_company_receipt_number",
            )
        ]
        indexes = [
            models.Index(fields=["company", "payment_date"]),
            models.Index(fields=["company", "status"]),
            models.Index(fields=["company", "client"]),
        ]

    def save(self, *args, **kwargs):
        if not self.receipt_number and self.pk is None:
            super().save(*args, **kwargs)
            self.receipt_number = (
                f"RCT-{timezone.localdate().year}-{self.pk:05d}"
            )
            super().save(update_fields=["receipt_number"])
            return

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()

        if self.client_id and self.company_id:
            if self.client.company_id != self.company_id:
                raise ValidationError({
                    "client": "Client must belong to this company."
                })

        if self.event_id and self.company_id:
            if self.event.company_id != self.company_id:
                raise ValidationError({
                    "event": "Event must belong to this company."
                })
            if self.client_id and self.event.client_id != self.client_id:
                raise ValidationError({
                    "event": "Event must belong to the selected client."
                })

        if self.quotation_id and self.company_id:
            if self.quotation.company_id != self.company_id:
                raise ValidationError({
                    "quotation": "Quotation must belong to this company."
                })
            if self.client_id and self.quotation.client_id != self.client_id:
                raise ValidationError({
                    "quotation": "Quotation must belong to the selected client."
                })
            if (
                self.event_id
                and self.quotation.event_id
                and self.quotation.event_id != self.event_id
            ):
                raise ValidationError({
                    "quotation": "Quotation belongs to a different event."
                })

        if self.status == self.Status.VOID and not self.void_reason:
            raise ValidationError({
                "void_reason": "A reason is required to void a payment."
            })

    def __str__(self):
        return self.receipt_number or f"Payment {self.pk}"


class Expense(models.Model):

    class Category(models.TextChoices):
        VENUE = "venue", "Venue"
        DECORATION = "decoration", "Decoration"
        CATERING = "catering", "Catering"
        TRANSPORT = "transport", "Transport"
        EQUIPMENT = "equipment", "Equipment"
        STAFF = "staff", "Staff"
        MARKETING = "marketing", "Marketing"
        UTILITIES = "utilities", "Utilities"
        OFFICE = "office", "Office"
        OTHER = "other", "Other"

    class Method(models.TextChoices):
        CASH = "cash", "Cash"
        UPI = "upi", "UPI"
        BANK = "bank", "Bank Transfer"
        CARD = "card", "Card"
        CHEQUE = "cheque", "Cheque"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        POSTED = "posted", "Posted"
        VOID = "void", "Void"

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="expenses",
    )
    event = models.ForeignKey(
        "events.Event",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses",
    )

    expense_number = models.CharField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=30,
        choices=Category.choices,
        default=Category.OTHER,
    )
    payee = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    expense_date = models.DateField(default=timezone.localdate)
    method = models.CharField(
        max_length=20,
        choices=Method.choices,
        default=Method.CASH,
    )
    transaction_reference = models.CharField(max_length=150, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    description = models.TextField(blank=True)
    void_reason = models.TextField(blank=True)
    posted_at = models.DateTimeField(null=True, blank=True)
    voided_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_expenses",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-expense_date", "-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["company", "expense_number"],
                name="unique_company_expense_number",
            )
        ]
        indexes = [
            models.Index(fields=["company", "expense_date"]),
            models.Index(fields=["company", "status"]),
            models.Index(fields=["company", "category"]),
        ]

    def save(self, *args, **kwargs):
        if not self.expense_number and self.pk is None:
            super().save(*args, **kwargs)
            self.expense_number = (
                f"EXP-{timezone.localdate().year}-{self.pk:05d}"
            )
            super().save(update_fields=["expense_number"])
            return

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()

        if self.event_id and self.company_id:
            if self.event.company_id != self.company_id:
                raise ValidationError({
                    "event": "Event must belong to this company."
                })

        if self.status == self.Status.VOID and not self.void_reason:
            raise ValidationError({
                "void_reason": "A reason is required to void an expense."
            })

    def __str__(self):
        return self.expense_number or self.title
