# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0015_auto_20170117_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='teashop.Category'),
        ),
    ]
