from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='index'),
  path('cars/<int:car_id>/', views.cars_detail, name='detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/add_comment/', views.add_comment, name='add_comment'),
  path('cars/<int:car_id>/add_review/', views.add_review, name='add_review'),
  # path('cars/<int:car_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
  path('reviews/', views.ReviewList.as_view(), name='reviews_index'),
  path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='reviews_detail'),
  path('reviews/create/', views.ReviewCreate.as_view(), name='reviews_create'),
  path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
  path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]