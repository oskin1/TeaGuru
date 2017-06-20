from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.OrderCreate, name='OrderCreate'),
    url(r'^options/$', views.OrderOptions, name='OrderOptions'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.AdminOrderDetail, name='AdminOrderDetail'),
#    url(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.AdminOrderPDF, name='AdminOrderPDF')
]
