from django.contrib.syndication.views import Feed
from blog.models import Post
from django.utils.safestring import mark_safe
from django.utils.encoding import force_str
import markdown2
import datetime
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render_to_response

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

def getSearchResults(request):
    """
    Search for a post by title or abstract. To search http://example.com/search?q=title
    """
    # Get the query data
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    # Query the database
    results = Post.objects.filter(Q(title__icontains=query) | Q(abstract__icontains=query))

    # Add pagination
    pages = Paginator(results, 5)

    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display the search results
    return render_to_response('blog/post_list.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': query})

