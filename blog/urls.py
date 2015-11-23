from django.conf.urls import patterns, url

from blog import views
from blog.models import Post
from django.views.generic import ListView, DetailView



urlpatterns = patterns('',
    #url(r'^$', views.index),
    #url(r'^Post/view/(?P<slug>[^\.]+).html',views.view_post,name='view_Post_post'),
    #url(r'^Post/category/(?P<slug>[^\.]+).html',views.view_category,name='view_Post_category'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$',views.PostView.as_view(),name='view_post'),
    url(r'^(?P<pk>\d+)/category/$',views.CategoryView.as_view(),name='view_blog_category'),
    # Index
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        ),
        name='index'
        ),
    # Individual posts
    url(r'^(?P<pub_date__year>\d{4})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        ),
        name='post'
        ),
)


#urlpatterns = []