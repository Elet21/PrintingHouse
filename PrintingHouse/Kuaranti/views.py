from django.shortcuts import render
from .models import Category


def index(requests):
    categories = Category.objects.all()
    # category = Category.objects.get(pk=id)
    # business_card = category.businesscard_set.all()
    return render(requests, 'main_page.html', {'categories': categories})


def list_category(requests, id):
    category = Category.objects.get(pk=id)
    business_card = category.businesscard_set.all()
    return render(requests, 'category_list.html', {'business_card': business_card})

