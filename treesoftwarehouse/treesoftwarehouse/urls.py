from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^djangoforms/', include('djangoforms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
