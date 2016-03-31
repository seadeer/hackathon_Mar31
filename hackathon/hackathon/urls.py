
from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.logreg.urls')),
]
