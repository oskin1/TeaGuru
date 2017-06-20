# -*- coding: utf-8 -*-
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.encoding import python_2_unicode_compatible
from teashop.models import Product, Service
from cupons.models import Cupon
from django.conf import settings
from yandex_money.models import Payment
from account.models import Account

@python_2_unicode_compatible
class Order(models.Model):
    
    STATUSES = (
        ('new', 'Новый'),
        ('complete', 'Завершён'),
        ('canceled', 'Отменён'),
        ('denied', 'Отклонён'),
        ('pending', 'Ожидает'),
        ('processing', 'В работе'),
        ('shipped', 'Доставлен'),
        ('voided', 'Аннулирован'),
        ('failed', 'Провален'),
    )
    
    payment_type = models.CharField(verbose_name='Способ оплаты', max_length=2, 
                                    choices=settings.PAYMENT_TYPE.CHOICES, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=180)
    last_name = models.CharField(verbose_name='Фамилия', max_length=180)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    telephone = models.CharField(verbose_name='Телефон', max_length=18)
    address =  models.CharField(verbose_name='Адрес', max_length=250)
    city = models.CharField(verbose_name='Город', max_length=100)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    payment = models.ForeignKey(Payment, verbose_name='Платёж', null=True, blank=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)
    cupon = models.ForeignKey(Cupon, related_name='orders', null=True, blank=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                          MaxValueValidator(100)])
    account = models.ForeignKey(Account, related_name='orders', verbose_name='Пользователь', null=True, blank=True)
    status = models.CharField(verbose_name='Статус', max_length=20, choices=STATUSES, default='new')

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return u'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        service_cost = sum(service.get_cost() for service in self.services.all())
        return total_cost - total_cost * (self.discount / Decimal('100')) + service_cost

@python_2_unicode_compatible
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

@python_2_unicode_compatible        
class ServiceItem(models.Model):
    order = models.ForeignKey(Order, related_name='services')
    service = models.ForeignKey(Service, related_name='order_services')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    
    def __str__(self):
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
