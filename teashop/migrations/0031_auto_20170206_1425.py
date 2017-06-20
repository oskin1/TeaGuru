# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0030_auto_20170202_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='metadata',
            field=models.TextField(blank=True, max_length=210, verbose_name='\u041c\u0435\u0442\u0430\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(blank=True, null=True, related_name='_product_related_products_+', to='teashop.Product'),
        ),
    ]