from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tdd.views.home', name='home'),
    # url(r'^tdd/', include('tdd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
    
)
