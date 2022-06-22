from django import forms
from .models import Labor


class NewLaborClassForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ["labor_class", "billing_code", "default_rates", "active"]
        labels = {'labor_class': "Labor Class",
                  'billing_code': "Billing Code",
                  'default_rates': "Default Rates",
                  'active': "Active"}



class NewSuppliesClassForm(forms.Form):
    class Meta:
        model = Labor
        fields = ["supplies_class", "billing_code", "default_rates", "active"]


class NewEquipmentClassForm(forms.Form):
    class Meta:
        model = Labor
        fields = ["equipment_class", "billing_code", "default_rates", "active"]
