from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from django.forms import ValidationError
from django.db.models import Prefetch
from .models import Order, OrderItem
from cart.models import Cart
from .forms import CreateOrderForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io


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

                product.quantity -= quantity
                product.save()

                # Очистить корзину пользователя после создания заказа
                cart_items.delete()
            return redirect('order_list')
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
    user= requests.user
    return render(requests, 'order/orders.html', {'orders': orders, 'user': user})


def download_pdf(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    # Создаем объект HttpResponse для отправки PDF файла
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order.id}.pdf"'

    # Создаем буфер для PDF
    buffer = io.BytesIO()

    # Создаем PDF файл с помощью ReportLab
    p = canvas.Canvas(buffer, pagesize=letter)

    # Определяем абсолютный путь к шрифту
    

    # Регистрация шрифта с поддержкой кириллицы
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'fonts/DejaVuSans.ttf'))
    p.setFont('DejaVuSans', 12)

    # Добавление текста на PDF в виде чека
    width, height = letter

    p.drawString(30, height - 50, "ИНФОРМАЦИЯ О ЗАКАЗЕ")
    p.line(30, height - 55, 580, height - 55)
    
    p.drawString(30, height - 80, f"Номер заказа: {order.id}")
    p.drawString(30, height - 100, f"Имя: {order.user.username}")
    p.drawString(30, height - 120, f"Номер телефона: +{order.phone_number}")
    
    # Пример добавления линии разделения
    p.line(30, height - 150, 580, height - 150)
    
    # Пример добавления информации о товаре
    p.drawString(30, height - 170, "Товары:")
    
    y = height - 190
    for item in order_items:
        p.drawString(50, y, f"{item.name} - {item.quantity} руб. x {item.price} руб. = {item.products_price()} руб.")
        y -= 30

    # Итоговая сумма
    total_amount = order_items.total_price()
    p.drawString(30, y, f"Итоговая сумма: {total_amount} руб.")
    
    p.line(30, y + 15, 580, y + 15)
    # Закрываем и сохраняем PDF файл
    p.showPage()
    p.save()

    # Получаем значение буфера и записываем его в ответ
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response