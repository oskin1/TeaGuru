# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import PopUp, Subscriber

class PopUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active',)
    list_editable = ('active',)
    class Meta:
        model = PopUp

admin.site.register(PopUp, PopUpAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_created',)

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)