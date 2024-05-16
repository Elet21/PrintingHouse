from ast import Delete
from django.shortcuts import redirect, render
from django.http import JsonResponse

from Kuaranti.models import Product
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


def cart_decrement(requests, product_id):
    product: Product = Product.objects.get(id=product_id)

    if requests.user.is_authenticated:
        carts = Cart.objects.filter(user=requests.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity -= 1
                cart.save()
        if cart.quantity < 1:
            carts.delete()

    return redirect(requests.META['HTTP_REFERER'])


def cart_remove(requests, cart_id):
    cart = Cart.objects.get(user=requests.user, id=cart_id)
    cart.delete()
    return redirect(requests.META['HTTP_REFERER'])



