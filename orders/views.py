# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import ServiceItem, OrderItem, Order
from teashop.models import Service
from .forms import OrderCreateForm, OrderOptionsForm
from cart.cart import Cart
from .tasks import OrderCreated, ManNotify
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
#import weasyprint


#@staff_member_required
#def AdminOrderPDF(request, order_id):
#    order = get_object_or_404(Order, id=order_id)
#    html = render_to_string('orders/order/pdf.html', {'order': order})
#    response = HttpResponse(content_type='application/pdf')
#    response['Content-Disposition'] = 'filename=order_{}.pdf'.format(order.id)
#    weasyprint.HTML(string=html).write_pdf(response,
#               stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/bootstrap.min.css')])
#    return response

@staff_member_required
def AdminOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.cupon:
                order.cupon = cart.cupon
                order.discount = cart.cupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            request.session['order_id'] = order.id
            return redirect(reverse('orders:OrderOptions'))

    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
                                                        
def OrderOptions(request):
    if request.method == 'POST':
        form = OrderOptionsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order_id = request.session['order_id']
            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                return render(request, 'payment_err.html', {'message':'Ошибка оформления заказа, попробуйте заново!'})
            order.payment_type = cd['payment_type']
            order.save()
            
            deliv = Service.objects.get(id=cd['deliv_method'])
            ServiceItem.objects.create(order=order, 
                                       service=deliv, 
                                       price=deliv.price)
            
            ManNotify.delay(order.id)
            OrderCreated.delay(order.id)
            
            if cd['payment_type'] == 'NC':
                return render(request, 'orders/order/created.html', {'order': order,})
            return redirect(reverse('payment:Process'))
    
    form = OrderOptionsForm()
    return render(request, 'orders/order/options.html', {'form': form})    
        
        
        
        
