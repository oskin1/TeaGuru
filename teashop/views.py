# -*- coding: utf-8 -*-
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.admin.views.decorators import staff_member_required
from .models import ShopConfig, Product, Category, Clist, Tag, ForeignPage, ForeignPageGroup, Set, Carousel, Slide
from blog.models import Post
from .filters import Facets, Fields
from .forms import UploadFileForm, ProductSearchForm, ExportProductsForm
from .constructors import *
import django_excel as excel
import datetime

def search(request):
    search_form = ProductSearchForm(request.GET)
    results_list = search_form.search()
    query = search_form.cleaned_data['q']
    results = construct_page(request, results_list[0])
    ctx = { 'results' : results, 'suggestions' : None, 'message' : None, 'query' : query }
    if results_list[0].query.backend.include_spelling:
        ctx['suggestion'] = search_form.get_suggestion()
    if not results_list[1]:
        ctx['message'] = 'Поиск не дал результатов'
        ctx['results'] = results[20:50]
    template = get_fragment(request, 'search/search.html')
    return render(request, template, ctx)

def index(request):
    carousel = Carousel.objects.get(slug='index_screen')
    popcats = Clist.objects.get(slug='pop_cats')
    posts = Post.objects.all().order_by('-pub_date')
    sets = Set.objects.filter(index=True)
    ctx = {
        'carousel' : carousel,
        'popcats' : popcats,
        'posts' : posts,
        'sets' : sets,
    }
    return render(request, 'index.html', ctx)

def product(request, category_slug=None, product_slug=None):
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    fields = Fields(product_slug)
    if not category_slug == None:
        category = Category.objects.get(slug=category_slug)
        ctx = { 'product': product, 'category': category, 'fields': fields, }
    else:
        ctx = { 'product': product, 'fields': fields, }
    return render(request, 'product_detail.html', ctx)

def category(request, category_slug=None):
    tags = request.GET.get('tags')
    if tags:
        t = tags.split(',')
        product_list = Product.objects.filter(category__slug=category_slug, 
                                                    tag__id__in=t, active=True).distinct()
    else:
        product_list = Product.objects.filter(category__slug=category_slug, active=True)
    products = construct_page(request, product_list)   
    category = Category.objects.get(slug=category_slug)
    facets = Facets(category_slug)
    ctx = {
        'category': category,
        'products': products,
        'facets': facets,
    }
    template = get_fragment(request, 'category.html')
    return render(request, template, ctx)
    
def set_list(request):
    set_list = Set.objects.filter(active=True)
    page = construct_page(request, set_list)
    ctx = {'page': page}
    return render(request, 'sets.html', ctx)
    
def set_detail(request, slug=None):
    ctx = {}
    ctx['set'] = Set.objects.get(slug=slug)
    return render(request, 'set_detail.html', ctx)
    
def info(request, slug=None):
    page = ForeignPage.objects.get(slug=slug)
    return render(request, 'info.html', {'page': page})
    
def sitemap(request):
    ctx = {}
    ctx['posts'] = Post.objects.all()
    return render(request, 'sitemap.html', ctx)

@staff_member_required
def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=Product,
                mapdict={'name':'name',
                         'slug':'slug',
                         'active':'active',
                         'price':'price',
                         'description':'description',
                         'brief':'brief',
                         'netto':'netto',
                         'unit':'unit',
                         'stock':'stock',
                         'duration':'duration',
                         'temperature':'temperature',
                         'volume':'volume',
                         'articul':'articul',})
            return redirect('admin:index')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    ctx = { 'form' : form, 'header' : 'Импорт товаров из файла' }
    template = loader.get_template('admin/import_form.html')
    return HttpResponse(template.render(ctx, request))
    
@staff_member_required
def export_data(request):
    if request.method == "POST":
        form = ExportProductsForm(request.POST, request.FILES)
        if form.is_valid():
            cat_slug = form.cleaned_data['slug']
            category = Category.objects.get(slug=cat_slug)
            qs = Product.objects.filter(category=category).distinct()
            column_names = ['articul', 'name', 'slug', 'price', 'netto', 'unit',]
            return excel.make_response_from_query_sets(
                qs,
                column_names,
                'xls',
                file_name=cat_slug
            )
        else:
            return HttpResponseBadRequest()
    else:
        form = ExportProductsForm()
    ctx = { 'form' : form, 'header' : 'Экспорт товаров в XLS' }
    template = loader.get_template('admin/import_form.html')
    return HttpResponse(template.render(ctx, request))    
