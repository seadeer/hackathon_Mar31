from django.conf.urls import patterns, url
from apps.findpad import views
urlpatterns = patterns('',
	url(r'^$', views.add, name='add'),
)