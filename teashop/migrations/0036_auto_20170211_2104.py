# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0035_auto_20170209_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('icon', models.ImageField(upload_to='icons', verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
                ('color', models.CharField(max_length=12, verbose_name='\u0426\u0432\u0435\u0442')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0434\u0430\u043b\u044c',
                'verbose_name_plural': '\u041c\u0435\u0434\u0430\u043b\u0438',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', to='teashop.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='teashop.Manufacturer', verbose_name='\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c'),
        ),
        migrations.AlterField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(blank=True, related_name='_product_related_products_+', to='teashop.Product', verbose_name='\u0421\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='products', to='teashop.Tag', verbose_name='\u0422\u0435\u0433\u0438'),
        ),
        migrations.AddField(
            model_name='product',
            name='awards',
            field=models.ManyToManyField(blank=True, related_name='products', to='teashop.Award', verbose_name='\u041c\u0435\u0434\u0430\u043b\u0438'),
        ),
    ]
