# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20170116_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.TextField(blank=True, max_length=220, verbose_name='\u0422\u0438\u0442\u0443\u043b'),
        ),
    ]
