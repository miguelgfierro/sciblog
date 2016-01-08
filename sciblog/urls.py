from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Admin panel
    url(r'^admin/', include(admin.site.urls)),
    # Blog URLs
    url(r'^', include('blog.urls', namespace="blog")),
    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
    url(r'^ckeditor/', include('libs.ckeditor_uploader.urls')),
)
