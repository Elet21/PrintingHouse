from ast import Delete
from django.shortcuts import redirect

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
    else:
        carts = Cart.objects.filter(
            session_key=requests.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=requests.session.session_key, product=product, quantity=1)
    


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
    else:
        carts = Cart.objects.filter(
        session_key=requests.session.session_key, product=product)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity -= 1
                cart.save()

    return redirect(requests.META['HTTP_REFERER'])


def cart_remove(requests, cart_id):
    if requests.user.is_authenticated:
        cart = Cart.objects.get(user=requests.user, id=cart_id)
    else: 
        cart = Cart.objects.get(session_key=requests.session.session_key, id=cart_id)
    cart.delete()
    return redirect(requests.META['HTTP_REFERER'])



