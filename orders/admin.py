# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Order, OrderItem, ServiceItem
from yandex_money.models import Payment
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import format_html
import csv
import datetime


def OrderDetail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))
OrderDetail.short_description = 'Инфо'

#def OrderPDF(obj):
#    return format_html('<a href="{}">PDF</a>'.format(
#        reverse('orders:AdminOrderPDF', args=[obj.id])
#    ))
#OrderPDF.short_description = 'В PDF'

def ExportToCSV(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Первая строка- оглавления
    writer.writerow([field.verbose_name for field in fields])
    # Заполняем информацией
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
    ExportToCSV.short_description = 'Export CSV'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    raw_id_field = ['service']

class OrderAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ['id', 'first_name', 'status', 'paid', 'get_total_cost', 'created',
                    OrderDetail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline, ServiceItemInline]
    actions = [ExportToCSV]

admin.site.register(Order, OrderAdmin)
