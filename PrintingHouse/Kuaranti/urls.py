from django.urls import path
from .views import index, list_category, category_detail, all_list

urlpatterns = [
    path('', index, name='main_page'),
    path("all/", all_list, name="all_list"),
    path('category/<int:id>/', list_category, name='category_detail'),
    path('category/subcategory/<int:id>', category_detail, name='subcategory_detail')
]