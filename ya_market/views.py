from django.shortcuts import render
from teashop.filters import Fields
from teashop.models import Product
import datetime

def yml_gen(request):
    products = Product.objects.all()
    items = {}
    for product in products:
        items[str(product.id)] = { 'product': product, 
                                   'fields': Fields(product.slug), }
    ctx = {}
    ctx['items'] = items.values()
    ctx['date'] = datetime.datetime.now()
    return render(request, 'market.xml', ctx)
