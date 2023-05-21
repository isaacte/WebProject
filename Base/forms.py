from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class ReviewForm(forms.ModelForm):
    qualification = forms.CharField(label='Rating', widget=forms.TextInput(attrs={'min':0,'max': '5','type': 'number'}))
    class Meta:
        model = Review
        fields =["qualification", "comment"]