from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .forms import RegisterForm, ReviewForm
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseNotFound
from .models import Author, BookInUserLibrary, Review
from django.shortcuts import get_object_or_404
import requests
from .utils import get_book

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

@login_required
def my_books(request):
    return render(request, 'Base/my_books.html')

def author(request, author_id):
    a = get_object_or_404(Author, openlibrary_key = author_id)
    return render(request, 'Base/author.html', {'author': a})

def book(request, book_id):
    b = get_book(book_id)
    if not b:
        return HttpResponseNotFound("Book not found.")
    a = b.authorinbook_set.all()
    g = b.literarygenreinbook_set.all()
    r = Review.objects.filter(book = b)
    form = ReviewForm()
    return render(request, 'Base/book.html', {'book': b, 'authors': a, 'genres': g, 'reviews': r, 'form': form})

@login_required
def create_review(request, book_id):
    if request.method != 'POST':
        return HttpResponseBadRequest(f"Method not allowed.", status=405)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.book = get_book(book_id)
        review.save()
        return redirect('book', book_id=book_id)
    form = ReviewForm()
    return redirect('book', book_id=book_id)

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
