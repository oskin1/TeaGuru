from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import *

sitemaps = {
    'categories': CategorySitemap,
    'products': ProductSitemap,
    'infopages': ForeignPageSitemap,
    'posts': BlogSitemap,
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sitemap/$', views.sitemap, name='Sitemap'),
    url(r'^search/$', views.search, name='Search'),
    url(r'^admin/teashop/import/products/$', views.import_data, name='ImportProducts'),
    url(r'^admin/teashop/export/products/$', views.export_data, name='ExportProducts'),
    url(r'^goods/(?P<product_slug>[-\w]+)/$', views.product, name='ProductIntView'),
    url(r'^info/(?P<slug>[-\w]+)/$', views.info, name='InfoPage'),
    url(r'^sets/(?P<slug>[-\w]+)/$', views.set_detail, name='SetDetail'),
    url(r'^sets/$', views.set_list, name='SetList'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<product_slug>[-\w]+)/$', views.product, name='ProductView'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category, name='CategoryView'),
    url(r'^$', views.index, name='Index'),
]
