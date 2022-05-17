from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Review(models.Model):
  name = models.CharField(max_length=1000)
  date = models.DateField('review date')

  def __str__(self):
    return f'{self.make} ({self.id})'

  def get_absolute_url(self):
    return reverse('reviews_detail', kwargs={'pk': self.id})

class Car(models.Model):
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.IntegerField()
  engine = models.CharField(max_length=50)
  mileage = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # might cause error
  # reviews = models.ManyToManyField(Review)
  reviews = models.ForeignKey(Review, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.make} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})


class Comment(models.Model):
  description = models.CharField(max_length=150)
  date = models.DateField('comment date')
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.make} ({self.id})'

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for car_id: {self.car_id} @{self.url}"