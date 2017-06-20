# -*- coding: utf-8 -*-
from django import forms


class CuponApllyForm(forms.Form):
    code = forms.CharField(label=u"Промокод")

class CuponGenerateForm(forms.Form):
    discount = forms.IntegerField(label=u"Скидка %")
    quantity = forms.IntegerField(label=u"Кол-во купонов")
    delta = forms.IntegerField(label=u"Период активности (дней)")