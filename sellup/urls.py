from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^subscribe/$', views.subscribe, name='Subscribe'),
    url(r'^unsubscribe/$', views.unsubscribe, name='Unsubscribe'),
]
