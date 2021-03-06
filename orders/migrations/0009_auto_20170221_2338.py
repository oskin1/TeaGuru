# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20170221_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(blank=True, choices=[(b'NC', '\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438 \u043f\u0440\u0438 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0438'), (b'PC', '\u041a\u043e\u0448\u0435\u043b\u0435\u043a \u042f\u043d\u0434\u0435\u043a\u0441.\u0414\u0435\u043d\u044c\u0433\u0438'), (b'AC', '\u0411\u0430\u043d\u043a\u043e\u0432\u0441\u043a\u0430\u044f \u043a\u0430\u0440\u0442\u0430'), (b'GP', '\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438 \u0447\u0435\u0440\u0435\u0437 \u043a\u0430\u0441\u0441\u044b \u0438 \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u044b'), (b'MC', '\u0421\u0447\u0435\u0442 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'), (b'WM', '\u041a\u043e\u0448\u0435\u043b\u0435\u043a WebMoney'), (b'SB', '\u0421\u0431\u0435\u0440\u0431\u0430\u043d\u043a: \u043e\u043f\u043b\u0430\u0442\u0430 \u043f\u043e SMS \u0438\u043b\u0438 \u0421\u0431\u0435\u0440\u0431\u0430\u043d\u043a \u041e\u043d\u043b\u0430\u0439\u043d'), (b'AB', '\u0410\u043b\u044c\u0444\u0430-\u041a\u043b\u0438\u043a'), (b'MA', 'MasterPass'), (b'PB', '\u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u0431\u0430\u043d\u043a \u041f\u0440\u043e\u043c\u0441\u0432\u044f\u0437\u044c\u0431\u0430\u043d\u043a\u0430'), (b'QW', 'QIWI Wallet'), (b'QP', '\u0414\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u043b\u0430\u0442\u0435\u0436 (\u041a\u0443\u043f\u043f\u0438.\u0440\u0443)')], max_length=2, verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xbe\xd1\x81\xd0\xbe\xd0\xb1 \xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8b'),
        ),
    ]
