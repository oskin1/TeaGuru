from uuid import uuid4
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from teashop.models import Product
from .cart import Cart
from .forms import CartAddOneProductForm, CartAddTenProductForm, CartAddProductForm
from cupons.forms import CuponApllyForm


@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
        if request.user_agent.is_mobile:
            return HttpResponse('OK', 200)
    return redirect('cart:CartMiniDetail')

def CartRemove(request, product_id):
    full = request.GET.get('full')
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    if not full:
        return redirect('cart:CartMiniDetail')
    return redirect('cart:CartDetail')

def CartMiniDetail(request):
    cart = Cart(request)
    return render(request, 'cart_mini_.html',
                 {'cart': cart,})

def CartDetail(request):
    cart = Cart(request)
    if cart.get_total_quantity() > 0:
        for item in cart:
            item['update_quantity_form_1'] = CartAddOneProductForm(
                                            initial={
                                                'quantity': item['quantity'],
                                                'update': True
                                            })
            item['update_quantity_form_10'] = CartAddTenProductForm(
                                            initial={
                                                'quantity': item['quantity'],
                                                'update': True
                                            })
        cupon_apply_form = CuponApllyForm()
        return render(request, 'cart_detail_.html',
                     {'cart': cart, 'cupon_apply_form': cupon_apply_form, 'ec_id': uuid4()})
    return redirect('teashop:Index')
    