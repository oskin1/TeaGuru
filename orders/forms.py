# -*- coding: utf-8 -*-
from django import forms
from .models import Order
from teashop.models import Service
from django.conf import settings

class OrderCreateForm(forms.ModelForm):
    telephone = forms.CharField(label=None, widget=forms.TextInput(
                                attrs={
                                    'type': 'tel',
                                    'placeholder': 'Номер телефона',
                                }
                            ))
    first_name = forms.CharField(label=None, widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Имя',
                                }
                            ))
    last_name = forms.CharField(label=None, widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Фамилия',
                                }
                            ))
    email = forms.CharField(label=None, widget=forms.EmailInput(
                                attrs={
                                    'placeholder': 'E-mail',
                                }
                            ))
    city = forms.CharField(label=None, widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Город',
                                }
                            ))
    address = forms.CharField(label=None, widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Адрес',
                                }
                            ))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'telephone', 'city', 'address',]

class OrderOptionsForm(forms.Form):
    services = Service.objects.filter(type='deliv')
    methods = ((s.id, u'{} (+{} руб.)'.format(s.name, s.price)) for s in services)
    
    payment_type = forms.ChoiceField(choices=settings.PAYMENT_TYPE.CHOICES, widget=forms.RadioSelect, label='Выберите способ оплаты:')
    deliv_method = forms.ChoiceField(choices=methods, widget=forms.RadioSelect, label='Выберите способ доставки:')