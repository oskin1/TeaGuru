# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0052_auto_20170317_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=120, unique=True, verbose_name='\u0427\u041f\u0423'),
        ),
    ]
