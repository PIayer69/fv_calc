from django import forms
from .models import EntryModel


class EntryForm(forms.ModelForm):
  class Meta:
    model = EntryModel
    fields = ['production', 'sent', 'retrieved', 'date']
    widgets = {'date': forms.DateInput(
      attrs={
      'class': 'myClass',
      'type': 'date'}
    )}