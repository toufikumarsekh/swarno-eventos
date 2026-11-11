from django import forms
from django.forms import inlineformset_factory

from apps.clients.models import Client
from apps.events.models import Event
from .models import Quotation, QuotationItem


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = [
            "client", "event", "title", "status",
            "issue_date", "valid_until",
            "terms_and_conditions", "notes",
        ]
        widgets = {
            "issue_date": forms.DateInput(attrs={"type": "date"}),
            "valid_until": forms.DateInput(attrs={"type": "date"}),
            "terms_and_conditions": forms.Textarea(attrs={"rows": 3}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        if company:
            self.fields["client"].queryset = Client.objects.filter(company=company)
            self.fields["event"].queryset = Event.objects.filter(company=company)
        self.fields["event"].required = False

    def clean(self):
        cleaned = super().clean()
        client = cleaned.get("client")
        event = cleaned.get("event")
        if event and client and event.client_id != client.id:
            self.add_error("event", "Select an event belonging to this client.")
        return cleaned


class QuotationItemForm(forms.ModelForm):
    class Meta:
        model = QuotationItem
        fields = [
            "description", "quantity", "unit", "unit_price",
            "discount_percent", "tax_percent",
        ]
        widgets = {
            "quantity": forms.NumberInput(attrs={"step": "0.01", "min": "0.01"}),
            "unit_price": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "discount_percent": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
            "tax_percent": forms.NumberInput(attrs={"step": "0.01", "min": "0", "max": "100"}),
        }


QuotationItemFormSet = inlineformset_factory(
    Quotation,
    QuotationItem,
    form=QuotationItemForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)


def build_item_formset(*args, **kwargs):
    return QuotationItemFormSet(*args, **kwargs)
