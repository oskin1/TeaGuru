# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0026_remove_product_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
