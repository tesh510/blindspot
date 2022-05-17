from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import uuid
import boto3
from .models import Car, Review, Photo
from .forms import CommentForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  reviews_car_doesnt_have = Review.objects.exclude(id__in=id_list)
  comment_form = CommentForm()
  id_list = car.review.all().values_list('id')
  reviews_car_doesnt_have = Review.objects.exclude(id__in=id_list)
  return render(request, 'cars/detail.html', {
    'car': car,
    'comment_form': comment_form,
    'reviews': reviews_car_doesnt_have
  })

@login_required
def add_comment(request, car_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.car_id = car_id
    new_comment.save()
  return redirect('detail', car_id=car_id)

@login_required
def assoc_review(request, car_id, review_id):
  Car.objects.get(id=car_id).reviews.add(review_id)
  return redirect('detail', car_id=car_id)

class ReviewList(LoginRequiredMixin, ListView):
  model = Review

class ReviewDetail(LoginRequiredMixin, DetailView):
  model = Review

class ReviewCreate(LoginRequiredMixin, CreateView):
  model = Review
  fields = '__all__'

class ReviewUpdate(LoginRequiredMixin, UpdateView):
  model = Review
  fields = ['name', 'color']

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  success_url = '/reviews/'


class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = ['make', 'model', 'year', 'engine', 'mileage']
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)


class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  fields = ['make', 'model', 'year', 'engine', 'mileage']


class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

@login_required
def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, car_id=car_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', car_id=car_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
