# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from teashop.models import Category

class Carousel(models.Model):
    slug = models.SlugField(verbose_name="Идентификатор карусели", max_length=120, unique=True, allow_unicode=True)

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'    

class Slide(models.Model):
    name = models.CharField(verbose_name="Название", max_length=120)
    carousel = models.ForeignKey(Carousel, related_name="slides")
    background = models.ImageField(upload_to="slides", verbose_name="Изображение слайда")
    title = models.TextField(verbose_name="Титул", max_length=220, blank=True)
    subtitle = models.TextField(verbose_name="Подстрочник", max_length=260, blank=True)
    button = models.BooleanField(verbose_name="Установить кнопку?", default=False)
    button_text = models.CharField(verbose_name="Текст кнопки", max_length=120, blank=True)
    link = models.URLField(verbose_name="Ссылка")
    