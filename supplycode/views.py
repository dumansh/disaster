from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from .forms import NewLaborClassForm, NewSuppliesClassForm, NewExpenseClassForm
from .models import Labor, Supply, Expense


def AddNewLaborClass(request):
    if request.method == "POST":
        form = NewLaborClassForm(request.POST)
        print(form)
        # return HttpResponse("hello")
        if form.is_valid():
            form.save()
            messages.success(request, 'Labor Code Saved')
            return redirect('dashboard')

    form = NewLaborClassForm()
    context = {
        "form": form
    }
    return render(request, 'add_new_labor_class.html', context)


def LaborListView(request):
    labors = Labor.objects.all()
    context = {
        "labors": labors
    }
    return render(request, 'labor.html', {"labors": labors})


def LaborEditView(request, id):
    labor = get_object_or_404(Labor, pk=id)
    if request.method == "POST":
        form = NewLaborClassForm(request.POST, instance=labor)

        if form.is_valid():
            form.save()
            messages.success(request, 'Labor Code Updated')
            return redirect('dashboard')

    form = NewLaborClassForm(instance=labor)
    context = {
        "form": form
    }
    print(form)
    return render(request, "labor_edit.html", context)


def SupplyListView(request):
    supplies = Supply.objects.all()
    context = {
        "supplies": supplies
    }
    return render(request, 'supply.html', context)


def SupplyCreate(request):
    if request.method == "POST":
        form = NewSuppliesClassForm(request.POST)
        print(form)
        # return HttpResponse("hello")
        if form.is_valid():
            form.save()
            messages.success(request, 'Supply Code Saved')
            return redirect('dashboard')

    form = NewSuppliesClassForm()
    context = {
        "form": form
    }
    return render(request, 'create_supply.html', context)


def SupplyEdit(request, id):
    supply = get_object_or_404(Supply, pk=id)
    if request.method == "POST":
        form = NewSuppliesClassForm(request.POST, instance=supply)

        if form.is_valid():
            form.save()
            messages.success(request, 'Supply Code Updated')
            return redirect('dashboard')

    form = NewSuppliesClassForm(instance=supply)
    context = {
        "form": form
    }
    print(form)
    return render(request, "edit_supply.html", context)

    # form = NewSuppliesClassForm()
    # context = {
    #     "form": form
    # }
    # return render(request, 'create_supply.html', context)


def ExpenseCreate(request):
    if request.method == "POST":
        form = NewExpenseClassForm(request.POST)
        print(form)
        # return HttpResponse("hello")
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense Code Saved')
            return redirect('dashboard')

    form = NewExpenseClassForm()
    context = {
        "form": form
    }
    return render(request, 'create_expense.html', context)


def ExpenseListView(request):
    expenses = Expense.objects.all()
    context = {
        "expenses": expenses
    }
    return render(request, 'expense.html', {"expenses": expenses})


def ExpenseEditView(request, id):
    expense = get_object_or_404(Expense, pk=id)
    if request.method == "POST":
        form = NewExpenseClassForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            messages.success(request, 'Expense Code Updated')
            return redirect('dashboard')

    form = NewExpenseClassForm(instance=expense)
    context = {
        "form": form
    }
    print(form)
    return render(request, "edit_expense.html", context)

