from django.conf.urls import patterns, url
from apps.findpad import views
urlpatterns = patterns('',
	url(r'^new$', views.new, name='new'),
	url(r'^create$', views.create, name='create'),
	url(r'^show$', views.show, name='show'),
	url(r'^listing/(?P<listing>\d+)', views.showOne, name='one'),
	url(r'^send/(?P<lister>\d+)', views.send, name='send'),
)