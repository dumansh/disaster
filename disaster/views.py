from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def login_page(request):
    return render(request, "login.html")
