from django.conf.urls import patterns, url

from waterplants import views

urlpatterns = patterns('',
    url(r'^waterplant/(?P<userplant_id>\d+)/$', views.index, name='waterplant'),
    url(r'^$', views.index, name='index'),
)

