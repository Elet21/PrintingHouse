from django.shortcuts import render
from .models import Category, SubCategory, Product
from .utils import search



def index(requests):
    categories = Category.objects.all()


    # category = Category.objects.get(pk=id)
    # business_card = category.businesscard_set.all()
    return render(requests, 'main_page.html', {'categories': categories})


def all_list(requests):
    subcategory = SubCategory.objects.all()
    categories = Category.objects.all()

    query = requests.GET.get('search', '')
    if query:
        subcategory = search(query)

    return render(requests, 'all_list.html', {'subcategory': subcategory, 'categories': categories })


def list_category(requests, id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=id)
    subcategory = category.subcategory_set.all()
    context = {
        'subcategory': subcategory, 
        'categories': categories,
        'category': category, 
    }        
    return render(requests, 'category_list.html', context)


def category_detail(requests, id):
    subcategory = SubCategory.objects.get(pk=id)
    subcategory_detail = subcategory.product_set.all()
    return render(requests, 'category_detail.html', {'subcategory_detail': subcategory_detail, 'subcategory': subcategory})


