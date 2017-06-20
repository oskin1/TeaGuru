# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teashop', '0038_service'),
        ('orders', '0005_order_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='orders.Order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_services', to='teashop.Service')),
            ],
        ),
    ]
