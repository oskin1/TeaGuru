# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0049_auto_20170308_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_descr',
            field=models.TextField(blank=True, max_length=660, verbose_name='\u041c\u0435\u0442\u0430-\u0442\u0435\u0433 description'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=360, verbose_name='\u041c\u0435\u0442\u0430-\u0442\u0435\u0433 title'),
        ),
    ]
