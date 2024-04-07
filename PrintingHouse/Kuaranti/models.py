from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class BusinessCard(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    img = models.ImageField(verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    rounding_corners = models.BooleanField(verbose_name='Скругленныые края')
    embossing = models.BooleanField(verbose_name='Тиснение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Визитка'
        verbose_name_plural = 'Визитки'



