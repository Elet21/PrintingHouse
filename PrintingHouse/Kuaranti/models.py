from pyexpat import model
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(verbose_name='Изображение', blank=True, upload_to='subcategory/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ПодКатегория'
        verbose_name_plural = 'ПодКатегории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    img = models.ImageField(verbose_name='Изображение')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



