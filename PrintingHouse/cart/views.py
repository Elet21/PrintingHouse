from django.shortcuts import redirect, render

from Kuaranti.models import Product
import user
from .models import Cart



def cart_add(requests, product_id):
    product = Product.objects.get(id=product_id)

    if requests.user.is_authenticated:
        carts = Cart.objects.filter(user=requests.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=requests.user, product=product, quantity=1)

    return redirect(requests.META['HTTP_REFERER'])


def cart_change(requests, cart_id):
    if requests.user.is_authenticated:
        cart = Cart.objects.get(user=requests.user, id=cart_id)
        


def cart_remove(requests, cart_id):
    cart = Cart.objects.get(user=requests.user, id=cart_id)
    cart.delete()
    return redirect(requests.META['HTTP_REFERER'])



