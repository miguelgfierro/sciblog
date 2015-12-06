from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class FlatpageSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return FlatPage.objects.all()