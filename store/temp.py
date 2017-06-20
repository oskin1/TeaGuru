from django.db import IntegrityError

from teashop.models import Product
from .models import StoreItem

def bind_prods(do=False):
    sis = StoreItem.objects.all()
    if do:
        for si in sis:
            if si.remainder != '0.00':
                try:
                    prod = Product.objects.get(store_item=si)
                except Product.DoesNotExist:
                    pass
                else:
                    prod.remainder = si.remainder
                    prod.save()
        return 'Done!'