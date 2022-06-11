from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']


class LoginForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['username']