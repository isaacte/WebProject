from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http.response import JsonResponse
from Base.forms import RegisterForm
from django.http import HttpRequest
from django.views import View
from .models import Book

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

class BookView(View):
    def get(self, request):
        books = list(Book.objects.values())

        if len(books) > 0:
            data = {'message': 'success', 'books': books}
        else:
            data = {'message': 'books not found'}
        return JsonResponse(data)


    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass