from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='index'),
  # path('cars/<int:car_id>/', views.cars_detail, name='detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  # path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  # path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  # path('cars/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  # path('cars/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  # path('cars/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  # path('cars/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
  # path('toys/', views.ToyList.as_view(), name='toys_index'),
  # path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  # path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  # path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  # path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]