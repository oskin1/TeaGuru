# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0024_auto_20170131_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='teashop.Category'),
        ),
    ]
