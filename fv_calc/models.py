from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class EntryModel(models.Model):
  user = models.ForeignKey(User, models.CASCADE)
  production = models.FloatField()
  sent = models.FloatField()
  retrieved = models.FloatField()
  date = models.DateField(default=now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"Entry of {self.user} from {self.date:%d/%m/%Y}"