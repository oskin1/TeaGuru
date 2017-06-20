# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from teashop.models import Product

@python_2_unicode_compatible
class Supplier(models.Model):
    name = models.CharField(verbose_name='Название', max_length=60)
    
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        
    def __str__(self):
        return self.name

class StoreItem(models.Model):
    product = models.ForeignKey(Product, 
                                related_name='store_item', 
                                verbose_name='Товар', 
                                on_delete=models.CASCADE)
    supplier = models.ManyToManyField(Supplier, 
                                      related_name='store_item', 
                                      verbose_name='Поставщик',
                                      blank=True)
    remainder = models.FloatField(verbose_name='Остаток на складе', default='0.00')
    date_upd = models.DateTimeField(verbose_name='UPD', auto_now=True)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'