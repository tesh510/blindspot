from django.contrib import admin
from .models import Car, Review, Comment, Photo

# Register your models here.

admin.site.register(Car)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Photo)

