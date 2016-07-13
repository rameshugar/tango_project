from django.conf.urls import patterns, include, url
from django.contrib import admin
# At the top of your urls.py file, add the following line:
from django.conf import settings

from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'add_page/(?P<category_name_slug>[\w\-]+)/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^register/$', views.register, name='register'), 
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),)
# UNDERNEATH your urlpatterns definition, add the following two lines:

    