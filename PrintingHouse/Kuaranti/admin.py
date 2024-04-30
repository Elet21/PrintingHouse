from django.contrib import admin
from .models import Category, BusinessCard, SubCategory

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(BusinessCard)