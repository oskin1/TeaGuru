# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0002_auto_20170114_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=160, unique=True, verbose_name='Tag name'),
        ),
    ]
