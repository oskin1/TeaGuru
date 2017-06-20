# -*- coding: utf-8 -*-
from celery import task
from django.core.mail import send_mail
from orders.models import Order

@task
def payment_succeed(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Оплата заказа {}'.format(order.id)
    message = 'Вы успешно оплатили заказ с номером {}. \
               Спасибо за покупку!'.format(order.id)
    mail_send = send_mail(subject, message, 'mailer@teaguru.me', [order.email])
    return mail_send

