# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 21:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0003_auto_20170114_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Discount %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=b'0.00', max_digits=10, verbose_name='Price per unit'),
        ),
    ]
