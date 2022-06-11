from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, LoginForm
from fv_calc.models import EntryModel


def home(request):
  entries = EntryModel.objects.all()
  context = {'entries': entries}
  return render(request, 'base/home.html', context)


def registerPage(request):
  if request.user.is_authenticated:
    return redirect('home')
    
  context = {'form': CustomUserCreationForm}
  return render(request, 'base/register.html', context)


def loginPage(request):
  if request.user.is_authenticated:
    return redirect('home')
    
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    
  context = {'form': LoginForm}
  return render(request, 'base/login.html', context)


def logoutPage(request):
  logout(request)
  return redirect('home')