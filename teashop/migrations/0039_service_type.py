# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0038_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.CharField(default='deliv', max_length=120, verbose_name='\u0422\u0438\u043f'),
            preserve_default=False,
        ),
    ]
