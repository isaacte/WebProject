# Base URL Configuration

from django.urls import include, path
from django.contrib.auth import views
from Base.views import menu

urlpatterns = [
    path('', menu, name='home'),
    #path('register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]