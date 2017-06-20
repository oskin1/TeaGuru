# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0031_auto_20170206_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='props',
            field=models.ManyToManyField(blank=True, related_name='categories', to='teashop.Property'),
        ),
        migrations.AlterField(
            model_name='foreignpage',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='pages', to='teashop.ForeignPageGroup'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', to='teashop.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(blank=True, related_name='_product_related_products_+', to='teashop.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='products', to='teashop.Tag'),
        ),
    ]
