# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0062_remove_product_remainder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remainder',
            field=models.FloatField(default='0.00', verbose_name='\u041e\u0441\u0442\u0430\u0442\u043e\u043a \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435'),
        ),
    ]
