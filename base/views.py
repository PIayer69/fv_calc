from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils.timezone import now
from .forms import CustomUserCreationForm, LoginForm
from fv_calc.models import EntryModel


def home(request):
  context = {}
  if request.user.is_authenticated:
    entries = EntryModel.objects.filter(user=request.user)
    months = entries.dates('date', 'month')
    sorted_entries = {}
    for month in months:
      if sorted_entries.get(month.year) is None:
        sorted_entries[month.year] = []
      sorted_entries[month.year].append({month.month: [e for e in entries if e.date.year == month.year and e.date.month == month.month]})
      
    for key, value in sorted_entries.items():
      print(key, value)
    print(now().year)
    
    context = {
      'entries': entries,
      'sorted_e': sorted_entries,
      'current_year': now().year,
    }
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