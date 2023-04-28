# Base URL Configuration

from django.urls import path
from django.contrib.auth import views
from Base.views import index, register

urlpatterns = [
    path('', index, name='home'),
    path('accounts/register/', register, name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='home'), name='logout'),
]