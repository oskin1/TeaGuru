# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellup', '0002_subscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a', 'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0438\u044b'},
        ),
        migrations.AddField(
            model_name='subscriber',
            name='active',
            field=models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u0435\u043d?'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
    ]
