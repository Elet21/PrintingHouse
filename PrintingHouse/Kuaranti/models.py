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


class BusinessCard(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    img = models.ImageField(verbose_name='Изображение')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    rounding_corners = models.BooleanField(verbose_name='Скругленныые края')
    embossing = models.BooleanField(verbose_name='Тиснение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Визитка'
        verbose_name_plural = 'Визитки'



