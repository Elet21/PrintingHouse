from django.shortcuts import render
from .models import Category, SubCategory


def index(requests):
    categories = Category.objects.all()
    print(type(categories))
    # category = Category.objects.get(pk=id)
    # business_card = category.businesscard_set.all()
    return render(requests, 'main_page.html', {'categories': categories})


def list_category(requests, id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=id)
    subcategory = category.subcategory_set.all()
    return render(requests, 'category_list.html', {'subcategory': subcategory, 'categories': categories})


def category_detail(requests, id):
    subcategory = SubCategory.objects.get(pk=id)
    subcategory_detail = subcategory.businesscard_set.all()
    return render(requests, 'category_detail.html', {'subcategory_detail': subcategory_detail})
