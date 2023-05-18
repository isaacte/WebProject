# Base URL Configuration

from django.urls import path, include
from django.contrib.auth import views
from rest_framework import routers
from Base.views import index, register, author, book, search_book, my_books
from .api import BookViewSet, AuthorInBookViewSet, AuthorViewSet, BooksFromUserSet

router = routers.DefaultRouter()

router.register('books', BookViewSet, 'books')
router.register('author', AuthorViewSet, 'author')
router.register('author-in-book', AuthorInBookViewSet, 'authorInBook')
router.register('user-books', BooksFromUserSet, 'booksFromUserSet')

urlpatterns = [
    path('', index, name='home'),
    path('my_books', my_books, name='my books'),
    path('accounts/register/', register, name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('author/<int:author_id>', author, name='author'),
    path('book/<str:isbn>', book, name='book'),
    path('api/search_book/<str:query>', search_book, name='search_book'),
    path('api/', include(router.urls)),
]