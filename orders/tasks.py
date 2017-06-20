# -*- coding: utf-8 -*-
from celery import task, shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import ServiceItem, OrderItem, Order

from templated_email import send_templated_mail

@task
def OrderCreated(order_id):

    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    order_servs = ServiceItem.objects.filter(order=order)
    mail_send = send_templated_mail(
                    template_name='new_order',
                    from_email='mailer@teaguru.me',
                    recipient_list=[order.email],
                    context={
                        'name': order.first_name,
                        'total': order.get_total_cost(),
                        'items': order_items,
                        'services': order_servs,
                        'order_id': order.id
                    },
                )
    
    return mail_send

@shared_task
def ManNotify(order_id):
    
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    order_servs = ServiceItem.objects.filter(order=order)
    staff = User.objects.filter(is_staff=True)
    
    receps = [s.email for s in staff]
    
    mail_send = send_templated_mail(
                    template_name='new_order_manager',
                    from_email='mailer@teaguru.me',
                    recipient_list=receps,
                    context={
                        'name': order.first_name,
                        'phone': order.telephone,
                        'total': order.get_total_cost(),
                        'items': order_items,
                        'services': order_servs
                    },
                )
    return mail_send
    
        