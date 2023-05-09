from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http.response import JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from Base.forms import RegisterForm
from django.http import HttpRequest
from django.views import View
from .models import Book, Author
from django.shortcuts import get_object_or_404

def register(request : HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    return render(request, 'Base/index.html')

def author(request, author_id):
    author = get_object_or_404(Author, id = author_id)
    return render(request, 'Base/author.html', {'author': author})