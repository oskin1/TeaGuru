from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ymlgen/$', views.yml_gen, name='YmlGen'),
]
