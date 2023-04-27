from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from Base.forms import RegisterForm
from django.http import HttpRequest

# Create your views here.
<<<<<<< HEAD
def index(request):
    return render(request, "Base/index.html")
=======

def register(request : HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    return render(request, 'Base/index.html')
>>>>>>> 44280f41c9b7c0bd205a17c27b2d0788422a5938
