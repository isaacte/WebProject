# Base URL Configuration

from django.urls import path, include
from django.contrib.auth import views
from rest_framework import routers
from Base.views import index, register
from .api import BookViewSet, AuthorInBookViewSet, AuthorViewSet

router = routers.DefaultRouter()

router.register('books', BookViewSet, 'books')
router.register('author', AuthorViewSet, 'author')
router.register('authorinbook', AuthorInBookViewSet, 'authorInBook')

urlpatterns = [
    path('', index, name='home'),
    path('accounts/register/', register, name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/', include(router.urls))
]