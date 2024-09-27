from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class User(Model):
    STATUS_CHOICES = (
        ('ukryte', 'Ukryte'),
        ('widoczne', 'Widoczne')
    )
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    zgloszono = models.DateTimeField(default=timezone.now)
    opis = models.CharField(max_length=15000)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='widoczne')



class MyAdmin(Model):
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
            super().save(*args, **kwargs)

# Create your models here.
