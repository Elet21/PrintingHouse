from django.db.transaction import commit
from django.shortcuts import render, redirect
from django.views import View
from .models import Order
from .forms import CreateOrderForm


# def create_order(requests):
#     return render(requests, 'order/create_order.html')


# def add_order(requests):
#     ...


class CreatOrder(View):

    def get(self, requests):
        context = {
            'forms': CreateOrderForm()
        }
        return render(requests, 'order/create_order.html', context)
    
    def post(self, request):
        user = request.user
        print(request.user)
        carts = user.cart_set.all()
        form = CreateOrderForm(request.POST)  
        if form.is_valid():
            print(form.cleaned_data['phone_number'])
            order = Order.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
            )
            order.cart.set(carts)
            # order = form.save(commit=False)
            # order.user = user
            # order.save()
            # order.cart.set(carts)
            return redirect('main_page')
        else:
            context = {
                'forms': form
            }
            print(form)
            print('Форма не валидна')
        return render(request, 'order/create_order.html', context)