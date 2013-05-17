from django.conf.urls.defaults import patterns, include, url
from djangoforms import views

urlpatterns = patterns('',
    url(r'^$', views.contact, name='contact')
)
