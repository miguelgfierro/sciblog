from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r"^", include("blog.urls", namespace="blog")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^ckeditor/", include("libs.ckeditor_uploader.urls")),
]
