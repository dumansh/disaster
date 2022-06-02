from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from .models import Labor


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
