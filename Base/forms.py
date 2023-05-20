from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =["qualification", "comment"]