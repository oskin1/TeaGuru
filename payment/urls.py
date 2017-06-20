# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^fail-payment/$', payment_fail, name='payment_fail'),
    url(r'^success-payment/$', payment_success, name='payment_success'),
    url(r'^$', payment_process, name='Process'),
]