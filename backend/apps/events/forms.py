from django import forms
from .models import Event
from apps.clients.models import Client
from apps.enquiries.models import Enquiry


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "client", "enquiry", "title", "event_type",
            "event_date", "start_time", "end_time",
            "venue", "guest_count", "budget",
            "status", "description", "notes",
        ]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company

        if company:
            self.fields["client"].queryset = Client.objects.filter(
                company=company
            )
            self.fields["enquiry"].queryset = Enquiry.objects.filter(
                company=company
            )

        self.fields["enquiry"].required = False

    def clean(self):
        cleaned = super().clean()
        client = cleaned.get("client")
        enquiry = cleaned.get("enquiry")

        if enquiry and client and enquiry.client_id != client.id:
            self.add_error(
                "enquiry",
                "Select an enquiry belonging to the chosen client."
            )

        return cleaned
