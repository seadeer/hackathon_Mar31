from django.conf.urls import *
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    # url(r'^login/?$', views.twitter_login, name='twitterlogin'),
    url(r'^logout/?$', views.twitter_logout, name='logout'),
    url(r'^login/authenticated/?$', views.twitter_authenticated),
    url(r'^home/$', views.home)
)