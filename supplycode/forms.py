from django import forms
from .models import Labor, Supply


class NewLaborClassForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ["labor_class", "billing_code", "default_rates", "active"]


class NewSuppliesClassForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["supply_code", "billing_code", "default_rates", "active"]


class NewEquipmentClassForm(forms.Form):
    class Meta:
        model = Labor
        fields = ["equipment_class", "billing_code", "default_rates", "active"]
