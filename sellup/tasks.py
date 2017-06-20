# -*- coding: utf-8 -*-
from celery import task, shared_task
from django.core.mail import send_mail

from cupons.generators import cupon_gen

@shared_task
def send_cupon(recepient):
    cupon = cupon_gen(discount=5)
    
    subject = u'Подписка на Чайного Гуру'
    message = u'Вы успешно подписались на рассылку Чайного Гуру! \
               Ваш купон на скидку 5%: {}, активен до {}'.format(cupon[0]['code'], cupon[0]['valid_to'])
    mail_send = send_mail(subject, message, 'mailer@teaguru.me', [recepient])
    return mail_send
    