# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0019_auto_20170120_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='articul',
            field=models.CharField(max_length=160, unique=True, verbose_name='\u0410\u0440\u0442\u0438\u043a\u0443\u043b'),
        ),
    ]
