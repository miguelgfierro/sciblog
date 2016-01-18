from django.conf.urls import include, url
from django.contrib import admin
import django

if django.VERSION >= (1, 8):
    urlpatterns = [
        url(r'^', include('blog.urls', namespace="blog")),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^ckeditor/', include('libs.ckeditor_uploader.urls')),
    ]
else:
    from django.conf.urls import patterns

    admin.autodiscover()
    urlpatterns = patterns(
        '',
        url(r'^', include('blog.urls', namespace="blog")),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^ckeditor/', include('libs.ckeditor_uploader.urls')),
    )