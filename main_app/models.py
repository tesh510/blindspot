from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Car(models.Model):  
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    engine = models.CharField(max_length=50, default = 'v8')
    mileage = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
      return f'{self.name} ({self.id})'
    def get_absolute_url(self):
      return reverse('detail', kwargs={'car_id': self.id})

