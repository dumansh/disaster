from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from .forms import NewLaborClassForm
from .models import Labor


def AddNewLaborClass(request):
    if request.method == "POST":
        form = NewLaborClassForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('dashboard'))

    elif request.method == "GET":
        form = NewLaborClassForm()

    return render(request, 'add_new_labor_class.html', {'form': form})


class AddNewwLaborClass(View):
    form_class = NewLaborClassForm
    template_name = '/templates/add_new_labor_class.html'

    def get(self, request, *args, **kwargs):
        form = NewLaborClassForm()
        return render(request.self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('dashboard'))

        return render(request, self.template_name, {'form': form})


class LaborListView(ListView):
    model = Labor
    context_object_name = 'all_labor_class'
    ordering = ['labor_class']
    queryset = Labor.disasterLabor.all()
    template_name = 'dashboard.html'


class LaborCreateView(CreateView):
    model = Labor
    context_object_name = 'labor'
    fields = ['labor_class', 'billing_code', 'default_rates', 'active']
    success_url = reverse_lazy('dashboard')


class LaborUpdateView(UpdateView):
    model = Labor
    context_object_name = 'labor'
    fields = ['labor_class', 'billing_code', 'default_rates', 'active']
    success_url = reverse_lazy('dashboard')
