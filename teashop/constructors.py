# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def order_qs(request, qs):
    order = request.GET.get('order')
    sort = request.GET.get('sort')
    if order == 'ASC':
        return qs.order_by(sort)
    elif order == 'DESC':
        return qs.order_by('-' + sort)
    else:
        return qs

def construct_page(request, qs):
    limit = request.GET.get('limit')
    page_num = request.GET.get('page')
    if not limit:
        limit = 30        
    ordered_qs = order_qs(request, qs)
    paginator = Paginator(ordered_qs, limit)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages) 
    return page
    
def get_fragment(request, template):
    if request.is_ajax():
        return 'fragments/' + template
    return template