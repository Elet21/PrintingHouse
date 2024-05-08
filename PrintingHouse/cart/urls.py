from django.urls import path
from .views import cart_add, cart_change, cart_remove


urlpatterns = [
    path('cart_add/<int:product_id>', cart_add, name='cart_add'),
    path('cart_change/<int:cart_id>', cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>', cart_remove, name='cart_remove')
]