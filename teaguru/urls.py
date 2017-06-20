from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from teashop.views import search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^filer/', include('filer.urls')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^yandex-money/', include('yandex_money.urls')),
    url(r'^yandex-market/', include('ya_market.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^copons/', include('cupons.urls', namespace='cupons')),
    url(r'^order/', include('orders.urls', namespace='orders')),
    url(r'^sellup/', include('sellup.urls', namespace='sellup')),
    url(r'^', include('teashop.urls', namespace='teashop')),
]
