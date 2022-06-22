from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('NewSupplyCode/', views.AddNewLaborClass, name='new_labor_class'),
    path('supply/', views.SupplyListView, name='list_supply'),
    path('supply/create', views.SupplyCreate, name='create_supply'),

]