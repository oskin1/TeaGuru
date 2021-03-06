# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 20:36
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0022_auto_20170123_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(allow_unicode=True, max_length=60, unique=True, verbose_name='\u0427\u041f\u0423')),
                ('body', ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043b\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b')),
                ('style', models.CharField(max_length=20, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f css (\u0438\u043c\u044f \u0444\u0430\u0439\u043b\u0430)')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043f. \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0414\u043e\u043f. \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='ForeignPageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(allow_unicode=True, max_length=60, unique=True, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u0441\u0442\u0440\u0430\u043d\u0438\u0446',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('order', 'name'), 'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442', 'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b'},
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='foreignpage',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, related_name='pages', to='teashop.ForeignPageGroup'),
        ),
    ]
