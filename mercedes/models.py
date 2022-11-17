from django.db import models
from django_countries.fields import CountryField


class Salon(models.Model):
    stamp = models.CharField(max_length=50, verbose_name='Марка авто')
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    providers = models.ForeignKey('Provider', on_delete=models.PROTECT, verbose_name='Поставщики')
    country_of_origin = CountryField(verbose_name='страна производитель')
    price = models.DecimalField(max_digits=15 ,decimal_places=2, verbose_name='Цена')
    specifications = models.TextField(max_length=500, verbose_name='Характеристики авто')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.stamp

    class Meta:
        ordering = ['time_create']
        verbose_name = 'Сеть салонов'
        verbose_name_plural = 'Сеть салонов'


class Provider(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название компании')
    founder = models.CharField(max_length=50, verbose_name='Основатель')
    email = models.EmailField(max_length=100, verbose_name='Электронный адрес')
    company_information = models.TextField(max_length=500, verbose_name='Информация о компании', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
