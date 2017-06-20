# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 17:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd')),
            ],
            options={
                'ordering': ('date_created',),
                'verbose_name': '\u041f\u0440\u043e\u043c\u043e \u043a\u043e\u0434',
                'verbose_name_plural': '\u041f\u0440\u043e\u043c\u043e \u043a\u043e\u0434\u044b',
            },
        ),
    ]