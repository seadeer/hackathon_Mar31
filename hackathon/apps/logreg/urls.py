from django.conf.urls import patterns, url
from apps.logreg import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^home$', views.home, name='home'),
)