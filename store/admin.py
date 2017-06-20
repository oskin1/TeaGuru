from django.contrib import admin

from .models import *

class SupplierAdmin(admin.ModelAdmin):
    class Meta:
        model = Supplier
        
admin.site.register(Supplier, SupplierAdmin)

class StoreItemAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    search_fields = ('product.name',)
    list_display = ('product', 'remainder', 'supplier',)
    list_editable = ('remainder',)
    filter_horizontal = ('supplier',)
    
    class Meta:
        model = StoreItem
        
admin.site.register(StoreItem, StoreItemAdmin)