from django.contrib import admin

from .models import Category, Bike

# Register your models here.
admin.site.register(Category)
admin.site.register(Bike)