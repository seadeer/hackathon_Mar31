from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^findpad/', include('apps.findpad.urls')),
   url(r'^', include('apps.logreg.urls')),
]