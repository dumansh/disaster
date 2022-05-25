from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.data['username'].lower()
            password = form.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # starting session for the given user so the server
                # remembers the user next time
                return redirect("dashboard")


    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def dashboard(request):
    return render(request, "dashboard.html")

