from django import forms
from apps.clients.models import Client
from .models import Enquiry, FollowUp


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            "client", "title", "event_type", "event_date",
            "guest_count", "venue", "budget", "source",
            "status", "description",
        ]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "budget": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
        }

    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["client"].queryset = Client.objects.filter(
            company=company
        ).order_by("name")


class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ["scheduled_at", "note"]
        widgets = {
            "scheduled_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "note": forms.Textarea(attrs={"rows": 3}),
        }
