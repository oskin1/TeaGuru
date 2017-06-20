from django.conf.urls import url
from . import views
from blog import views

urlpatterns = [
    url(r'^(?P<slug>\w{0,60})/$', views.postDetail, name='PostDetail'),
    url(r'^$', views.postList, name='PostList'),
]
