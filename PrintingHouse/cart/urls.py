from django.urls import path
from .views import cart_add, cart_decrement, cart_remove


urlpatterns = [
    path('cart_add/<int:product_id>', cart_add, name='cart_add'),
    path('cart_remove/<int:cart_id>', cart_remove, name='cart_remove'),
    path('car_decrement/<int:product_id>', cart_decrement, name='cart_decrement')
]