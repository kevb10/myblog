from django.conf.urls import patterns, url
from myblog import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<post_id>\d+)/$', views.more,  name='more'),
    url(r'^new/$', views.new,  name='new'),
    url(r'^(?P<id>\d+)/delete/$', views.delete,  name='delete'),
    url(r'^all/$', views.paging, name="all"),
)
