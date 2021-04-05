from blog.models import Post
from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from django.contrib.sites.models import Site
from blog.sitemap import PostSitemap, FlatpageSitemap
from blog.views import (
    PostsFeed,
    get_search_results,
    IndexListView,
    PostDetailView,
    responsive_flatpage,
)


# Define sitemaps
sitemaps = {"posts": PostSitemap, "pages": FlatpageSitemap}

# Define robots.txt content
current_site = Site.objects.get_current()
robots_content = "User-agent: *\nDisallow: /admin/\nSitemap: https://{}/sitemap.xml".format(
    current_site.domain
)

urlpatterns = patterns(
    "",
    # Index
    url(r"^(?P<page>\d+)?/?$", IndexListView.as_view(), name="index",),
    # Individual posts
    url(
        r"^blog/(?P<pub_date__year>\d{4})/(?P<slug>[a-zA-Z0-9-]+)/?$",
        PostDetailView.as_view(),
        name="post",
    ),
    # Post RSS feed
    url(r"^feed/posts/$", PostsFeed()),
    # Search posts
    url(r"^search", get_search_results, name="search"),
    # robots.txt
    url(
        r"^robots.txt$",
        lambda r: HttpResponse(robots_content, content_type="text/plain"),
    ),
    # sitemap
    url(
        r"^sitemap\.xml$",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
)
# add flat pages
urlpatterns += patterns(
    "django.contrib.flatpages.views",
    url(r"^about/$", responsive_flatpage, {"url": "/about/"}, name="about"),
    url(r"^privacy/$", responsive_flatpage, {"url": "/privacy/"}, name="privacy"),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

