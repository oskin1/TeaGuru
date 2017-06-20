# -*- coding: utf-8 -*-
from django.contrib import admin
from suit.admin import SortableModelAdmin
from suit.admin import SortableStackedInline
from .models import *

class ShopConfigAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name',)
    fieldsets = [
        ('Common', {'fields': ['title', 'phone', 'location', 'currency', 'keywords_meta',]}),
    ]

admin.site.register(ShopConfig, ShopConfigAdmin)

class ForeignPageGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
    class Meta:
        model = ForeignPageGroup
        
admin.site.register(ForeignPageGroup, ForeignPageGroupAdmin)

class ForeignPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)
    filter_horizontal = ('group',)
    class Meta:
        model = ForeignPage
        
admin.site.register(ForeignPage, ForeignPageAdmin)

class PropertyAdmin(admin.ModelAdmin):
    class Meta:
        model = Property
        
admin.site.register(Property, PropertyAdmin)

class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'level', 'active', 'order',)
    list_editable = ('active', 'order',)
    filter_horizontal = ('props',)
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'parent', 'level', 'order', 'title', 'active', 'preview', 'props',]}),
        ('SEO', {'fields': ['meta_title', 'meta_descr', 'meta_kwds',]}),
    ]

admin.site.register(Category, CategoryAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name',)
    fieldsets = [
        (None, {'fields': ['name', 'description', 'slug', 'image',]}),
    ]   

admin.site.register(Manufacturer, ManufacturerAdmin) 

class TagAdmin(admin.ModelAdmin):
    list_filter = ('prop',)
    fields = ('name', 'prop',)

admin.site.register(Tag, TagAdmin)

class AwardAdmin(admin.ModelAdmin):
    class Meta:
        model = Award
        
admin.site.register(Award, AwardAdmin)

class ProductImageInline(SortableStackedInline):
    model = ProductImage
    extra = 0
    fk_name = 'product'
    suit_classes = 'suit-tab suit-tab-general'
    sortable = 'order'

class OptionalProductFieldInline(admin.StackedInline):
    model = OptionalProductField
    extra = 1
    fk_name = 'product'
    suit_classes = 'suit-tab suit-tab-additional'

class ProductAdmin(SortableModelAdmin):
    search_fields = ('name', 'articul',)
    filter_horizontal = ('category', 'tag', 'related_products', 'awards',)
    empty_value_display = '-empty-'
    list_display = ('name', 'price', 'active', 'rating', 'remainder',)
    list_editable = ('price', 'active', 'rating', 'remainder',)
    list_filter = ('unit', 'active', 'stock', 'category')
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name', 'slug', 'articul', 'category', 'related_products', 'awards', 
                      'rating', 'manufacturer', 'active', 'stock', 'remainder', 'is_bundle',]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-pricing',),
            'fields': ['price', 'opt_price', 'zak_price', 'discount', 'netto', 'unit',]
        }),
        ('Инструкция', {
            'classes': ('suit-tab', 'suit-tab-additional',),
            'fields': ['duration', 'temperature', 'volume',]
        }),
        ('Мета-данные', {
            'classes': ('suit-tab', 'suit-tab-additional',),
            'fields': ['description', 'brief', 'tag', 'metadata',]
        }),
    ]
    suit_form_tabs = (('general', 'Общая информация'), ('pricing', 'Цены'), ('additional', 'Доп. информация'),)
    sortable = 'order'
    inlines = [ProductImageInline, OptionalProductFieldInline]

admin.site.register(Product, ProductAdmin)

class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service
        
admin.site.register(Service, ServiceAdmin)

class SetAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)
    empty_value_display = '-empty-'
    list_display = ('name', 'active', 'index')
    list_editable = ('active', 'index',)
    fieldsets = [
        ('Common', {'fields': ['name', 'slug', 'products', 'description', 'active', 'image', 'index',]}),
    ]

admin.site.register(Set, SetAdmin)

class ClistAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    filter_horizontal = ('category',)
    list_display = ('slug',)
    fieldsets = [
        ('Common', {'fields': ['slug', 'category',]}),
    ]

admin.site.register(Clist, ClistAdmin)

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