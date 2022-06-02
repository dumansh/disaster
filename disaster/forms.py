from django import forms
from .models import Labor


class NewLaborClassForm(forms.Form):
    class Meta:
        model = Labor
        fields = ["labor_class", "billing_code", "default_rates", "active"]

