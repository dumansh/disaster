from django import forms
from .models import Labor, Supply, Expense


class NewLaborClassForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ["labor_class", "billing_code", "default_rates", "active"]


class NewSuppliesClassForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["supply_code", "billing_code", "default_rates", "active"]


class NewEquipmentClassForm(forms.ModelForm):
    pass
    # class Meta:
    #    model = Equipment
    #    fields = ["equipment_code", "billing_code", "default_rates", "active"]


class NewExpenseClassForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["expense_code", "billing_code", "default_rates", "active"]
