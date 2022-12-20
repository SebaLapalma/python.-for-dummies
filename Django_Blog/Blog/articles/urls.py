from django.urls import path
from django.urls import re_path as url 
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.articles_list, name='list'),
    url(r'create/$', views.article_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]
