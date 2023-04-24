from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def menu(request):
    return render(request, 'Base/base.html')
