# -*- coding: utf-8 -*-
from django.shortcuts import render
from orders.models import Order
from .tasks import payment_succeed
from yandex_money.forms import PaymentForm
from yandex_money.models import Payment
    
def payment_process(request):
    try:
        order_id = request.session['order_id']
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return render(request, 'payment_err.html', {'message':'Ошибка оформления заказа, попробуйте заново!'})
    except KeyError:
        return render(request, 'payment_err.html', {'message':'Заказ не найден!'})
    
    amount = order.get_total_cost()
    
    payment = Payment(order_amount=amount, payment_type=order.payment_type, 
                      cps_phone=order.telephone, cps_email=order.email)
    payment.save()
    
    order.payment = payment
    order.save()

    ctx = {}
    ctx['payment_form'] = PaymentForm(instance=payment)
    ctx['payment'] = payment
    
    return render(request, 'payment.html', ctx)
    
def payment_success(request):
    ctx = {}
    ctx['message'] = 'Оплата прошла успешно. Спасибо за покупку!'
    try:
        order_id = request.session['order_id']
    except KeyError:
        ctx['order_id'] = 'Утерян! Возможно, вы очистили историю браузера?'
    else:
        payment_succeed(order_id)
        ctx['order_id'] = order_id
    
    return render(request, 'payment_finished.html', ctx)
    
def payment_fail(request):
    ctx = {}
    ctx['message'] = 'Что то пошло не так! Оплата не удалась.'
    try:
        ctx['order_id'] = request.session['order_id']
    except KeyError:
        ctx['order_id'] = 'Утерян! Возможно, вы очистили историю браузера?'
    
    return render(request, 'payment_finished.html', ctx)
    