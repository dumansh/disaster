from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('labor/', views.LaborListView, name='list_labor'),
    path('labor/create', views.AddNewLaborClass, name='new_labor_class'),
    path('labor/edit/<int:id>', views.LaborEditView, name='edit_labor'),

    path('supply/', views.SupplyListView, name='list_supply'),
    path('supply/create', views.SupplyCreate, name='create_supply'),
    path('supply/edit/<int:id>', views.SupplyEdit, name='edit_supply'),

    path('expense/', views.ExpenseListView, name='list_expense'),
    path('expense/create', views.ExpenseCreate, name='create_expense'),
    path('expense/edit/<int:id>', views.ExpenseEditView, name='edit_expense')

]