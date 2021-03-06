# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Category name')),
                ('title', models.CharField(max_length=60, verbose_name='Category title')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Unique category slug')),
                ('level', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3')], verbose_name='Category level')),
                ('active', models.BooleanField(default=False, verbose_name='Enable category?')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Order')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='teashop.Category')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Manufacturer name')),
                ('description', models.TextField(blank=True, max_length=501, verbose_name='Manufacturer description')),
                ('image', models.ImageField(blank=True, upload_to=b'images', verbose_name='Image')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Unique manufacturer slug')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='OptionalProductField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Field name')),
                ('value', models.TextField(max_length=501, verbose_name='Field value')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Product name')),
                ('slug', models.SlugField(max_length=60, null=True, unique=True, verbose_name='Unique product slug')),
                ('active', models.BooleanField(default=False, verbose_name='Enable product?')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Discount %')),
                ('description', models.TextField(blank=True, max_length=501, null=True, verbose_name='Product description')),
                ('brief', models.CharField(max_length=60, verbose_name='Brief descr for cat. view')),
                ('netto', models.PositiveIntegerField(verbose_name='Netto mass')),
                ('preview', models.ImageField(upload_to=b'images', verbose_name='Product preview image')),
                ('unit', models.CharField(choices=[(b'\xd0\xba\xd0\xb3', b'\xd0\xba\xd0\xb3.'), (b'\xd0\xb3\xd1\x80', b'\xd0\xb3\xd1\x80.'), (b'\xd1\x88\xd1\x82', b'\xd1\x88\xd1\x82.')], max_length=11, verbose_name='Unit')),
                ('stock', models.BooleanField(default=False, verbose_name='Is in stock?')),
                ('category', models.ManyToManyField(related_name='products', to='teashop.Category')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='teashop.Manufacturer')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description', models.CharField(blank=True, max_length=60, null=True, verbose_name='Meta description')),
                ('image', models.ImageField(upload_to=b'images', verbose_name='Product image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='teashop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Set name')),
                ('slug', models.SlugField(max_length=60, null=True, unique=True, verbose_name='Unique set slug')),
                ('description', models.TextField(blank=True, max_length=501, verbose_name='Set description')),
                ('image', models.ImageField(blank=True, upload_to=b'images', verbose_name='Set image')),
                ('active', models.BooleanField(default=False, verbose_name='Enable set?')),
                ('product', models.ManyToManyField(related_name='sets', to='teashop.Product')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u0431\u043e\u0440\u043a\u0430',
                'verbose_name_plural': '\u041f\u043e\u0434\u0431\u043e\u0440\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='ShopConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'teaguru', max_length=20, verbose_name='shop name')),
                ('title', models.CharField(max_length=60, verbose_name='shop title')),
                ('phone', models.CharField(max_length=18, verbose_name='phone number')),
                ('location', models.CharField(blank=True, max_length=75, verbose_name='shop location')),
                ('currency', models.CharField(blank=True, max_length=10, verbose_name='currency (icon)')),
                ('keywords_meta', models.CharField(blank=True, max_length=90, null=True, verbose_name='Keywords meta')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430',
                'verbose_name_plural': '\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Tag name')),
                ('prop', models.CharField(choices=[(b'c', b'\xd1\x86\xd0\xb2\xd0\xb5\xd1\x82'), (b'e', b'\xd1\x8d\xd1\x84\xd1\x84\xd0\xb5\xd0\xba\xd1\x82'), (b'm', b'\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7-\xd0\xbb\xd1\x8c')], max_length=30, verbose_name='Tag property')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u0433',
                'verbose_name_plural': '\u0422\u0435\u0433\u0438',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='teashop.Tag'),
        ),
        migrations.AddField(
            model_name='optionalproductfield',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='teashop.Product'),
        ),
    ]
