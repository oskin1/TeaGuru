# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0047_product_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('order', 'name'), 'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442', 'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b'},
        ),
    ]
