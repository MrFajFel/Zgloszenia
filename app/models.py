from django.db import models
from django.db import models
from django.db.models import Model
from django.utils import timezone


class User(Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    zgloszono = models.DateTimeField(default=timezone.now)
    opis = models.CharField(max_length=1000)
# Create your models here.
