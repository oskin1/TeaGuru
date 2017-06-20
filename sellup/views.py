# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import SubscribeForm, UnsubscribeForm
from .models import Subscriber
from .tasks import send_cupon

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            send_cupon.delay(form.cleaned_data['email'])
            form.save()

            return HttpResponse(200, 'OK')
            
        return HttpResponse(400, 'Bad Request')
            
    return HttpResponse(405, 'Method Not Allowed')
    
def unsubscribe(request):
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                subscr = Subscriber.objects.get(email=email)
            except Subscriber.DoesNotExist:
                return HttpResponse(212, 'Does Not Exist')
            
            subscr.active = False
            subscr.save()
            
            return HttpResponse(200, 'OK')
      
    form = UnsubscribeForm()
    return render(request, 'unsubscribe.html', {'form':form})