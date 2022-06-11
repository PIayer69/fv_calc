from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import EntryModel


# Create your views here.
def addData(request):
  if request.method == "POST":
    form = EntryForm(request.POST)
    if form.is_valid:
      entry = form.save(commit=False)
      entry.user = request.user
      entry.save()
      return redirect('home')
  
  context = {
    'form': EntryForm,
    'site': 'add'
  }
  return render(request, 'fv_calc/data_form.html', context)


def editData(request, pk):
  entry = EntryModel.objects.get(id=pk)

  if request.method == "POST":
    entry = EntryForm(request.POST, instance=entry)
    
  
  form = EntryForm(instance=entry)
  context = {
    'form': form,
    'site': 'edit'
  }
  return render(request, 'fv_calc/data_form.html', context)


def deleteData(request, pk):
  entry = EntryModel.objects.get(id=pk)
  entry.delete()
  return redirect('home')