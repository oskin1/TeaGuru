# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0063_product_remainder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_bundle',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0440\u043e\u0434\u0443\u043a\u0442 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043d\u0430\u0431\u043e\u0440\u043e\u043c?'),
        ),
    ]
