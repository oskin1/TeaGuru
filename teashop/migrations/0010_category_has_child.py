# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0009_auto_20170115_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='has_child',
            field=models.BooleanField(default=False, verbose_name='Has child?'),
        ),
    ]
