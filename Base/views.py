from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
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

@login_required
def my_reviews(request):
    return render(request, 'Base/my_reviews.html', {'reviews': request.user.review_set.all()})

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
    if request.user.is_authenticated:
        rbu = b.read_by_user(request.user)
    else:
        rbu = False
    if request.user.is_authenticated:
        ur = Review.objects.filter(user = request.user, book = b).exists()
    else:
        ur = False
    return render(request, 'Base/book.html', {'book': b, 'authors': a, 'genres': g, 'reviews': r, 'user_review_exists': ur, 'read_by_user': rbu})

@login_required
def create_review(request, book_id):
    b = get_book(book_id)
    if not b:
        return HttpResponseNotFound("Book not found.")
    a = b.authorinbook_set.all()
    g = b.literarygenreinbook_set.all()
    r = Review.objects.filter(book = b)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = b
            review.save()
            return redirect('book', book_id)
    else:
        form = ReviewForm()
    return render(request, 'Base/create_review.html', {'book': b, 'authors': a, 'genres': g, 'reviews': r, 'form': form})

@login_required
def edit_review(request, book_id):
    b = get_book(book_id)
    if not b:
        return HttpResponseNotFound("Book not found.")
    a = b.authorinbook_set.all()
    g = b.literarygenreinbook_set.all()
    r = Review.objects.filter(book = b)
    ur = Review.objects.get(user = request.user, book = b)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=ur)
        if form.is_valid():
            form.save()
            return redirect('book', book_id)
    else:
        form = ReviewForm(instance = ur)
    return render(request, 'Base/edit_review.html', {'book': b, 'authors': a, 'genres': g, 'reviews': r, 'form': form})

@login_required
def delete_review(request, book_id):
    b = get_book(book_id)
    ur = get_object_or_404(Review, book = b, user=request.user)
    ur.delete()
    return redirect('book', book_id = book_id)

def subject(request, sub):
    return render(request, 'Base/subject.html', {'subject': sub})

@login_required
def save_book(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(f"Method not allowed.", status=405)
    b = get_book(request.POST.get('book_id'))
    if b:
        if not b.read_by_user(request.user) and request.POST.get('action') == 'add':
            BookInUserLibrary.objects.create(book = b, user=request.user)
            return HttpResponse('')
        elif b.read_by_user(request.user) and request.POST.get('action') == 'remove':
            BookInUserLibrary.objects.get(book=b, user=request.user).delete()
            return HttpResponse('')
        return HttpResponseBadRequest("Book already in your library.")

    return HttpResponseBadRequest("Book not found.")
