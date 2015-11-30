from django.conf.urls import patterns, url
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Index
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        ),
        name='index'
        ),
    # Individual posts
    url(r'^blog/(?P<pub_date__year>\d{4})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        ),
        name='post'
        ),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


