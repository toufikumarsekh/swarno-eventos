from django import forms
from .models import Payment, Expense
from apps.clients.models import Client
from apps.events.models import Event
from apps.quotations.models import Quotation


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = (
            "client", "event", "quotation", "payment_type",
            "amount", "payment_date", "method",
            "transaction_reference", "notes",
        )
        widgets = {
            "payment_date": forms.DateInput(attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"step": "0.01", "min": "0.01"}),
        }

    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["client"].queryset = Client.objects.filter(company=company)
        self.fields["event"].queryset = Event.objects.filter(company=company)
        self.fields["quotation"].queryset = Quotation.objects.filter(company=company)

    def clean(self):
        cleaned = super().clean()
        client = cleaned.get("client")
        event = cleaned.get("event")
        quotation = cleaned.get("quotation")

        if event and client and event.client_id != client.pk:
            self.add_error("event", "This event does not belong to the selected client.")

        if quotation and client and quotation.client_id != client.pk:
            self.add_error("quotation", "This quotation does not belong to the selected client.")

        if quotation and event and quotation.event_id and quotation.event_id != event.pk:
            self.add_error("quotation", "This quotation belongs to a different event.")

        return cleaned


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = (
            "title", "category", "payee", "event",
            "amount", "expense_date", "method",
            "transaction_reference", "description",
        )
        widgets = {
            "expense_date": forms.DateInput(attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"step": "0.01", "min": "0.01"}),
        }

    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"].queryset = Event.objects.filter(company=company)


class VoidReasonForm(forms.Form):
    reason = forms.CharField(
        label="Reason for voiding",
        min_length=5,
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Explain why this transaction is being voided.",
        }),
    )
