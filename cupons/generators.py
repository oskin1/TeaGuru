from uuid import uuid4
from datetime import timedelta
from random import randint

from django.utils import timezone
from django.db import IntegrityError
from .models import Cupon

def cupon_gen(qty=1, days=30, discount=0):
    now = timezone.now()
    valid_to = now + timedelta(days=days)
    i = 0
    cupons = []
    while i < qty:
        code = '{}-{}-{}-{}'.format(randint(100, 999), 
                                    randint(100, 9999), 
                                    randint(100, 999), 
                                    randint(100, 9999))
        try:
            cupon = Cupon.objects.create(code=code,
                                         valid_from=now,
                                         valid_to=valid_to,
                                         discount=discount,
                                         active=True)
        except IntegrityError:
            pass
        else:
            cupons.append({
                'code': str(code),
                'valid_to': valid_to,
            })
            i += 1
    return cupons