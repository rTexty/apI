from django.contrib import admin
from .models import Car, Brand, Category
# Register your models here.

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Category)