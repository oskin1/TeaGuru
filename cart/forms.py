# -*- coding: utf-8 -*-
from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 2000)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label=None, choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

PRODUCT_QUANTITY_CHOICES_1 = [(i, str(i) + 'шт.') for i in range(1, 11)]

class CartAddOneProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label=None, choices=PRODUCT_QUANTITY_CHOICES_1, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

PRODUCT_QUANTITY_CHOICES_10 = [(i*50, str(i*50) + 'гр.') for i in range(1, 21)]

class CartAddTenProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label=None, choices=PRODUCT_QUANTITY_CHOICES_10, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    
PRODUCT_QUANTITY_CHOICES_OPT = [(i*500, str(i*500) + 'гр.') for i in range(1, 21)]

class CartOptProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label=None, choices=PRODUCT_QUANTITY_CHOICES_10, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)