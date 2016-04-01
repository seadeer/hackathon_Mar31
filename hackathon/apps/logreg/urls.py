from django.conf.urls import *
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^login/twitter/$', views.login_twitter, name='twitterlogin'),
    url(r'^logout/?$', views.logout_twitter),
    url(r'^home/?$', views.home),
)