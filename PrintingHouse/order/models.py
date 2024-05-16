from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь", default=None)
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    cart = models.ManyToManyField(to=Cart, blank=True, null=True, verbose_name="Корзины", default=None)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.username} {self.user.last_name}"