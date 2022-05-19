from django.forms import ModelForm
from .models import Comment, Review

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['description']

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['description', 'rating']