# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0041_auto_20170226_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442', 'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
    ]
