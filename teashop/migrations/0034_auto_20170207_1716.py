# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0033_auto_20170206_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('order', 'name'), 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='foreignpage',
            options={'ordering': ('order', 'name'), 'verbose_name': '\u0414\u043e\u043f. \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430', 'verbose_name_plural': '\u0414\u043e\u043f. \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'},
        ),
        migrations.AlterField(
            model_name='foreignpage',
            name='style',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f css (\u0438\u043c\u044f \u0444\u0430\u0439\u043b\u0430)'),
        ),
    ]
