from django import forms
from .models import Company


class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "legal_name",
            "email",
            "phone",
            "gstin",
            "address",
            "city",
            "state",
            "country",
        ]

        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
        }
