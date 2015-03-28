from django.conf.urls import patterns, url

from waterplants import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)