from django.conf.urls import *
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^login/?$', views.twitter_login, name='twitterlogin'),
    url(r'^twlogout/?$', views.twitter_logout, name='twitter_logout'),
	url(r'^logout$', views.logout, name='logout'),
    url(r'^login/authenticated/?$', views.twitter_authenticated),
	url(r'^createUser$', views.createUser, name='createUser'),
	url(r'^login$', views.login, name='login'),
    url(r'^home/$', views.home, name='home')
)