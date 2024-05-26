from django.urls import path
from .views import CreatOrder, order_list


urlpatterns = [
    path('create-order/', CreatOrder.as_view(), name='create_order'),
    path('orders/', order_list, name='order_list')
]