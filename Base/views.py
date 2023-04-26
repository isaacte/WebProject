from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import models

# Create your views here.

class RegisterView(CreateView):
    model = models.User
    fields = ['username', 'password1', 'password2']

def menu(request):
    return render(request, 'Base/base.html')
