# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Cupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()
    date_created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('date_created',)
        verbose_name = 'Промо код'
        verbose_name_plural = 'Промо коды'    