# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_keywords_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]