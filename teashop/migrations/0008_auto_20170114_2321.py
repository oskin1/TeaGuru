# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0007_auto_20170114_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='duration',
            field=models.CharField(blank=True, max_length=160, verbose_name='Boiling duration'),
        ),
        migrations.AlterField(
            model_name='product',
            name='temperature',
            field=models.CharField(blank=True, max_length=160, verbose_name='Boiling temp'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.CharField(blank=True, max_length=160, verbose_name='Volume'),
        ),
    ]
