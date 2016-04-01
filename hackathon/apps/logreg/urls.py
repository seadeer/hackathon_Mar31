from django.conf.urls import patterns, url
from apps.logreg import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^home$', views.home, name='home'),
	url(r'^createUser$', views.createUser, name='createUser'),
	url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),
)