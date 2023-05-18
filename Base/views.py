from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http.response import JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from Base.forms import RegisterForm
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseNotFound
from django.views import View
from .models import Book, Author, BookInUserLibrary
from django.shortcuts import get_object_or_404
import requests
from .utils import  get_book

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
    a = get_object_or_404(Author, id = author_id)
    return render(request, 'Base/author.html', {'author': a})

def book(request, key):
    b = get_book(key)
    if not b:
        return HttpResponseNotFound("Book not found.")
    a = b.authorinbook_set.all()
    return render(request, 'Base/book.html', {'book': b, 'authors': a})

def search_book(request, query):
    result = requests.get(f'https://openlibrary.org/search.json?q={query}')
    return JsonResponse(result.json())

def subject(request, sub):
    return render(request, 'Base/subject.html', {'subject': sub})

def save_book(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(f"Method not allowed.", status=405)
    b = get_book(request.POST.get('book_id'))
    if b:
        if not BookInUserLibrary.objects.filter(book = b, user = request.user).exists():
            BookInUserLibrary.objects.create(book = b, user=request.user)
            return JsonResponse(200, {})
        return HttpResponseBadRequest("Book already in your library.")
    return HttpResponseBadRequest("Book not found.")
