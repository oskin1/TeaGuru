from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError
from .models import Cupon
from .forms import CuponApllyForm, CuponGenerateForm
from .generators import cupon_gen


@require_POST
def CuponApply(request):
    now = timezone.now()
    form = CuponApllyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            cupon = Cupon.objects.get(code__iexact=code,
                                      valid_from__lte=now,
                                      valid_to__gte=now,
                                      active=True)
        except Cupon.DoesNotExist:
            request.session['cupon_id'] = None
        else:
            request.session['cupon_id'] = cupon.id
            cupon.active = False
            cupon.save()
            
    return redirect('cart:CartDetail')

@staff_member_required
def GenerateCupons(request):
    if requst.method == 'POST':
        form = CuponGenerateForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            discount = form.cleaned_data['discount']
            delta = form.cleaned_data['discount']
            
            cupon_gen(quantity, delta, discount)
        return redirect('admin:index')
    
    form = CuponGenerateForm()
    return render(request, 'admin/import_form.html', {'form':form})
    