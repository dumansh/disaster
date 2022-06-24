from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from .forms import NewLaborClassForm, NewSuppliesClassForm
from .models import Labor, Supply


def AddNewLaborClass(request):
    if request.method == "POST":
        form = NewLaborClassForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

        form = NewLaborClassForm()

    elif request.method == "GET":
        form = NewLaborClassForm()

    return render(request, 'add_new_labor_class.html', {'form': form})


def LaborListView(request):
    labors = Labor.objects.all()

    return render(request, 'labor.html', {"labors": labors})


def LaborEditView(request):
    if request.method == "GET":
        data = request.GET
        obj = Labor.objects.get()
        if obj:
            initial_data = {
                Labor.labor_class, Labor.billing_code, Labor.default_rates, Labor.active
            }
            form = NewLaborClassForm(initial=data)

    elif request.method == "POST":
        form = NewLaborClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_labor')

    return render(request, 'labor_edit.html')


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


    form=NewSuppliesClassForm(instance=supply)
    context={
        "form":form
    }
    print(form)
    return render(request, "edit_supply.html",context)

    # form = NewSuppliesClassForm()
    # context = {
    #     "form": form
    # }
    # return render(request, 'create_supply.html', context)

