from django.contrib.syndication.views import Feed
from blog.models import Post
from django.utils.safestring import mark_safe
from django.utils.encoding import force_str
import markdown2
import datetime

class PostsFeed(Feed):
    title = "Sciblog - A blog designed like a scientific Latex paper"
    description = "Sciblog - A blog designed like a scientific Latex paper. Posts are about business, startups, science, artificial intelligence and machine learning."
    link = '/'

    def items(self):
        return Post.objects.order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        extras = ["fenced-code-blocks"]
        content = mark_safe(markdown2.markdown(force_str(item.abstract), extras = extras))
        return content

    def item_author_name(self, item):
        return item.authors

    def item_pubdate(self, item):
        return datetime.datetime.combine(item.pub_date, datetime.time())