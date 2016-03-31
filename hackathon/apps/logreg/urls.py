from django.conf.urls import *
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/twitter/$', include(social.apps.django_app.urls, namespace='social'), name='twitterlogin'),
    url(r'^logout/?$', views.twitter_logout),
    # twitter-authenticated:
    url(r'^home/?$', views.home),
)