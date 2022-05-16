from django.shortcuts import render, redirect
from .models import Car
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', { 'cars': cars })

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


class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = ['make', 'model', 'year', 'engine', 'mileage']
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)