# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

from teashop.models import Product

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=220)
    
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    slug = models.SlugField(verbose_name='Уникальная подпись', max_length=120, unique=True, allow_unicode=True)
    author = models.CharField(verbose_name='Автор (Чайный Гуру по умолчанию)', max_length=120, default='Чайный Гуру', blank=True)
    pub_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    rel_products = models.ManyToManyField(Product, related_name='posts', verbose_name='Связанные продукты', blank=True)
    title = models.CharField(verbose_name='Заголовок', max_length=220)
    teaser = models.TextField(verbose_name='Подстрочник', max_length=180)
    body = RichTextField(verbose_name='Статья')
    preview = models.ImageField(verbose_name='Превью', upload_to='blog')
    active = models.BooleanField(verbose_name='Активировать?', default=False)
    meta_kwds = models.TextField(verbose_name='Мета-тег keywords', max_length=660, blank=True)
    
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog:PostDetail', args=[self.slug])
