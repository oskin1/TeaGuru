# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse
from decimal import Decimal
from ckeditor.fields import RichTextField

@python_2_unicode_compatible
class ShopConfig(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20, default='teaguru')
    title = models.CharField(verbose_name='Title', max_length=260)
    phone = models.CharField(verbose_name='Тел. номер', max_length=18)
    location = models.CharField(verbose_name='Адрес', max_length=75, blank=True)
    currency = models.CharField(verbose_name='Иконка валюты', max_length=10, blank=True)
    keywords_meta = models.TextField(verbose_name='Мета-ключи', max_length=390, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Конфигурация магазина'
        verbose_name_plural = 'Конфигурации магазина'        

@python_2_unicode_compatible
class ForeignPageGroup(models.Model):
    name = models.CharField(verbose_name='Название', max_length=160, unique=True)
    slug = models.SlugField(verbose_name='Подпись', max_length=60, unique=True, allow_unicode=True)
    order = models.IntegerField(verbose_name='Порядок сортировки', blank=True, null=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Группа страниц'
        verbose_name_plural = 'Группы страниц' 
        
@python_2_unicode_compatible
class ForeignPage(models.Model):
    name = models.CharField(verbose_name='Название', max_length=160, unique=True)
    slug = models.SlugField(verbose_name='ЧПУ', max_length=60, unique=True, allow_unicode=True)
    group = models.ManyToManyField(ForeignPageGroup, related_name='pages', blank=True)
    body = RichTextField(verbose_name='Тело страницы')
    style = models.CharField(verbose_name='Дополнительная css (имя файла)', max_length=20, blank=True, null=True)
    order = models.IntegerField(verbose_name='Порядок сортировки', blank=True, null=True)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('teashop:InfoPage', args=[self.slug])
        
    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Доп. страница'
        verbose_name_plural = 'Доп. страницы'

@python_2_unicode_compatible       
class Property(models.Model):
    name = models.CharField(verbose_name='Название', max_length=160, unique=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры' 

@python_2_unicode_compatible
class Category(models.Model):
    LEVELS = [(i, str(i)) for i in range(1, 4)]
    name = models.CharField(verbose_name='Название', max_length=160, unique=True)
    parent = models.ForeignKey('self', related_name='child', null=True, blank=True)
    title = models.CharField(verbose_name='Заголовок', max_length=260)
    slug = models.SlugField(verbose_name='ЧПУ', max_length=60, unique=True, allow_unicode=True)
    level = models.IntegerField(verbose_name='Уровень', choices=LEVELS)
    active = models.BooleanField(verbose_name='Активировать?', default=False)
    order = models.IntegerField(verbose_name='Порядок вывода', blank=True, null=True)
    preview = models.ImageField(verbose_name='Превью', upload_to='previews', null=True, blank=True)
    props = models.ManyToManyField(Property, related_name='categories', blank=True)
    
    meta_title = models.CharField(verbose_name='Мета-тег title', max_length=360, blank=True)
    meta_descr = models.TextField(verbose_name='Мета-тег description', max_length=660, blank=True)
    meta_kwds = models.TextField(verbose_name='Мета-тег keywords', max_length=660, blank=True)

    def check_child(self):
        return self.child.all().exists()
        
    def get_absolute_url(self):
        return reverse('teashop:CategoryView', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order', 'level',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'                 

@python_2_unicode_compatible
class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Название', max_length=160, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=561, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images', blank=True)
    slug = models.SlugField(verbose_name='ЧПУ', max_length=60, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name    

    class Meta:
        ordering = ('name',)
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'        

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=160, unique=True)
    prop = models.ForeignKey(Property, related_name='tags', null=True, blank=True)

    def __str__(self):
        return self.name 
        
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'        

@python_2_unicode_compatible
class Award(models.Model):
    name = models.CharField(verbose_name='Название', max_length=160, unique=True)
    icon = models.CharField(verbose_name='Название иконки', max_length=42)
    color = models.CharField(verbose_name='Цвет', max_length=12)
    
    def __str__(self):
        return self.name 
        
    class Meta:
        verbose_name = 'Медаль'
        verbose_name_plural = 'Медали'     

@python_2_unicode_compatible
class Product(models.Model):
    UNITS = (
        ('kg', 'кг.'),
        ('gr', 'гр.'),
        ('wt', 'шт.'),
    )
    STARS =  [(i, str(i) + ' star(s)') for i in range(1, 6)]
    
    name = models.CharField(verbose_name='Название', max_length=160)
    slug = models.SlugField(verbose_name='ЧПУ', max_length=160, unique=True, null=True, allow_unicode=True)
    articul = models.CharField(verbose_name='Артикул', max_length=160, unique=True)
    metadata = models.TextField(verbose_name='Метаинформация', max_length=310, blank=True)
    category = models.ManyToManyField(Category, related_name='products', verbose_name='Категории', blank=True)
    tag = models.ManyToManyField(Tag, related_name='products', verbose_name='Теги', blank=True)
    related_products = models.ManyToManyField('self', related_name='related_products', verbose_name='Связанные продукты', blank=True)
    awards = models.ManyToManyField(Award, related_name='products', verbose_name='Медали', blank=True)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', verbose_name='Производитель',
                                                    blank=True, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(verbose_name='Активировать?', default=False)
    is_bundle = models.BooleanField(verbose_name='Продукт является набором?', default=False)
    
    price = models.DecimalField(verbose_name='Цена за одну единицу', max_digits=10, decimal_places=2, default="0.00")
    opt_price = models.DecimalField(verbose_name='Оптовая цена за одну единицу', max_digits=10, decimal_places=2, default="0.00")
    zak_price = models.DecimalField(verbose_name='Закупочная цена за одну единицу', max_digits=10, decimal_places=2, default="0.00")
    
    discount = models.IntegerField(verbose_name='Скидка %', blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    brief = models.CharField(verbose_name='Краткое описание', max_length=160)
    netto = models.PositiveIntegerField(verbose_name='Масса нетто')
    unit = models.CharField(verbose_name='Единицы измерения', choices=UNITS, max_length=11)
    stock = models.BooleanField(verbose_name='В наличии?', default=False)
    
    duration = models.CharField(verbose_name='Время заваривания', max_length=180, blank=True, null=True)
    temperature = models.CharField(verbose_name='Температура заваривания', max_length=180, blank=True, null=True)
    volume = models.CharField(verbose_name='Объём на чайник', max_length=180, blank=True, null=True)
    
    order = models.IntegerField(verbose_name='Порядок сортировки', blank=True, null=True)
    ordering = models.IntegerField(verbose_name='Порядок сортировки', blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    rating = models.IntegerField(verbose_name='Рейтинг', default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], choices=STARS)
    
    remainder = models.FloatField(verbose_name='Остаток на складе', default='0.00')

    def get_price(self):
        if self.discount:
            return round(self.price * ((100 - self.discount) / Decimal(100)), 2)
        return self.price

    def get_full_price(self):
        return self.price * self.netto
        
    def get_opt_price(self):
        return self.opt_price * self.netto

    def get_full_discount(self):
        return round((self.price * self.netto) * ((100 - self.discount) / Decimal(100)), 2)
        
    def get_margin(self):
        return u'{}%, {}руб.'.format(
            round((self.get_price() - self.zak_price) / (self.zak_price / Decimal(100)), 2),
            self.get_price() - self.zak_price
        )

    def get_absolute_url(self):
        return reverse('teashop:ProductIntView', args=[self.slug])    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order', 'name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'      

class ProductImage(models.Model):
    meta_description = models.CharField(verbose_name='Мета-описание', max_length=60, null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to="images")
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name='Порядок сортировки', blank=True, null=True)
    
    class Meta:
        ordering = ('order', 'id',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class OptionalProductField(models.Model):
    name = models.CharField(verbose_name='Название', max_length=60)
    value = models.TextField(verbose_name='Значение', max_length=501)
    product = models.ForeignKey(Product, related_name='fields', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительные поля'

@python_2_unicode_compatible        
class Service(models.Model):
    SERVICE_TYPES = (
        ('deliv', 'Способ доставки'),
        ('packg', 'Упаковка'),
    )
    
    name = models.CharField(verbose_name='Название', max_length=120)
    type = models.CharField(verbose_name='Тип', max_length=20, choices=SERVICE_TYPES)
    price = models.DecimalField(verbose_name='Цена за одну единицу', max_digits=10, decimal_places=2, default="0.00")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

@python_2_unicode_compatible
class Set(models.Model):
    name = models.CharField(verbose_name='Название', max_length=60)
    slug = models.SlugField(verbose_name='ЧПУ', max_length=120, unique=True, allow_unicode=True)
    products = models.ManyToManyField(Product, related_name='sets')
    description = models.TextField(verbose_name='Описание', max_length=501, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to="images", blank=True)
    active = models.BooleanField(verbose_name='Активировать?', default=False)
    index = models.BooleanField(verbose_name='Показывать на главной?', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
        
class Clist(models.Model):
    slug = models.SlugField(verbose_name="Идентификатор подборки", max_length=120, unique=True, allow_unicode=True)
    category = models.ManyToManyField(Category, related_name='clists')
    
    class Meta:
        verbose_name = 'Подборка категорий'
        verbose_name_plural = 'Подборки категорий'  
        
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
    order = models.IntegerField(verbose_name='Порядок сортировки', blank=True, null=True)
    
    class Meta:
        ordering = ('order', 'name',)
