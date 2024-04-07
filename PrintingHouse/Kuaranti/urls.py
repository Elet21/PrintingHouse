from django.urls import path
from .views import index, list_category

urlpatterns = [
    path('', index, name='main_page'),
    path('category/<int:id>/', list_category, name='category_detail')
]