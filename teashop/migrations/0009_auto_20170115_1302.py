# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0008_auto_20170114_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=120, unique=True, verbose_name='Unique category slug'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=120, unique=True, verbose_name='Unique manufacturer slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=160, null=True, unique=True, verbose_name='Unique product slug'),
        ),
        migrations.AlterField(
            model_name='set',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=120, null=True, unique=True, verbose_name='Unique set slug'),
        ),
    ]
