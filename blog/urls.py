from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='view_blog_post'),
    #url(r'^blog/category/(?P<slug>[^\.]+)$',views.view_category,name='view_blog_category'),
)