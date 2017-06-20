# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class SlideInline(admin.StackedInline):
    model = Slide
    extra = 1
    fk_name = 'carousel'

class CarouselAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('slug',)
    fieldsets = [
        ('Common', {'fields': ['slug',]}),
    ]
    inlines = [SlideInline,]

admin.site.register(Carousel, CarouselAdmin)

