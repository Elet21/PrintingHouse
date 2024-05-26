from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from django.forms import ValidationError
from django.db.models import Prefetch
from .models import Order, OrderItem
from cart.models import Cart
from .forms import CreateOrderForm


@method_decorator(login_required, name='dispatch')
class CreatOrder(View):

    def get(self, requests):
        context = {
            'forms': CreateOrderForm()
        }
        return render(requests, 'order/create_order.html', context)
    
    def post(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        form = CreateOrderForm(request.POST) 
        if form.is_valid():
            order = Order.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
            )
            for cart_item in cart_items:
                product=cart_item.product
                name=cart_item.product.name
                price=cart_item.product.price
                quantity=cart_item.quantity

                if product.quantity < quantity:
                    raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')
                OrderItem.objects.create(
                    order=order,
                    product= product,
                    name=name,
                    price=price,
                    quantity=quantity,
                )
            return redirect('main_page')
        else:
            context = {
                'forms': form
            }
        return render(request, 'order/create_order.html', context)
    

def order_list(requests):
    orders = Order.objects.filter(user=requests.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")
    for order in orders:
        print(order.created_ti)
    user= requests.user
    return render(requests, 'order/orders.html', {'orders': orders, 'user': user})