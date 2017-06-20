# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ckeditor.fields import RichTextField

@python_2_unicode_compatible
class PopUp(models.Model):
    name = models.CharField(verbose_name='Название', max_length=160)
    slug = models.SlugField(verbose_name='Подпись',
                            max_length=60, unique=True,
                            allow_unicode=True)
    body = RichTextField(verbose_name='Тело окна')
    active = models.BooleanField(default=False)
    duration = models.DurationField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Subscriber(models.Model):
    email = models.EmailField(verbose_name='E-mail', unique=True)
    date_created = models.DateTimeField(verbose_name='Дата подписки', auto_now_add=True)
    active = models.BooleanField(verbose_name='Активен?', default=True)
    
    def __str__(self):
        return self.email
        
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'