import os
import markdown2
import datetime

from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.encoding import force_str
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import get_template
from django.template.base import TemplateDoesNotExist
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.flatpages.views import render_flatpage
from django.contrib.flatpages.models import FlatPage
from django.http import Http404, HttpResponsePermanentRedirect

from blog.models import Post


def get_desktop_or_mobile_template(request, path, page):
    """Get template view from middleware depending on whether it is desktop or mobile

    Args:
        request (obj): Request object
        path (str): Path to the template
        page (str): html file of the template

    Returns:
        str: Path to template
    """
    try:
        template = os.path.join(request.template_prefix, path, page)
        get_template(template)
    except TemplateDoesNotExist:
        template = os.path.join(settings.DESKTOP_TEMPLATE_PREFIX, path, page)
    return template


class IndexListView(ListView):
    model = Post
    paginate_by = 5

    def get_template_names(self, *args, **kwargs):
        return get_desktop_or_mobile_template(self.request, "blog", "post_list.html")


class PostDetailView(DetailView):
    model = Post

    def get_template_names(self, *args, **kwargs):
        return get_desktop_or_mobile_template(self.request, "blog", "post_detail.html")


class PostsFeed(Feed):
    title = "Sciblog - A blog designed like a scientific LaTeX paper"
    description = "Sciblog - A blog designed like a scientific LaTeX paper. Posts are about business, startups, science, artificial intelligence and machine learning."
    link = "/"

    def items(self):
        return Post.objects.order_by("-pub_date")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        extras = ["fenced-code-blocks"]
        content = mark_safe(markdown2.markdown(force_str(item.abstract), extras=extras))
        return content

    def item_author_name(self, item):
        return item.authors

    def item_pubdate(self, item):
        return datetime.datetime.combine(item.pub_date, datetime.time())


def get_search_results(request):
    """Search for a post by title or abstract. To search http://example.com/search?q=title

    Args:
        request (obj): Request object

    """
    # Get the query data
    query = request.GET.get("q", "")
    page = request.GET.get("page", 1)

    # Query the database
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(abstract__icontains=query)
    )

    # Add pagination
    pages = Paginator(results, 5)

    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display the search results
    return render_to_response(
        get_desktop_or_mobile_template(request, "blog", "post_list.html"),
        {
            "page_obj": returned_page,
            "object_list": returned_page.object_list,
            "search": query,
        },
    )


def responsive_flatpage(request, url):
    """Custom flatpage that changes the template based on middleware depending on 
    whether it is desktop or mobile.
    Based of https://github.com/django/django/blob/stable/1.8.x/django/contrib/flatpages/views.py

    Args:
        request (obj): Request object
        url (str): URL of flat page, for example: /about/

    """
    if not url.startswith("/"):
        url = "/" + url
    site_id = get_current_site(request).id
    try:
        f = get_object_or_404(FlatPage, url=url, sites=site_id)
    except Http404:
        if not url.endswith("/"):
            url += "/"
            f = get_object_or_404(FlatPage, url=url, sites=site_id)
            return HttpResponsePermanentRedirect("%s/" % request.path)
        else:
            raise
    if f.template_name:
        f.template_name = request.template_prefix + "/" + f.template_name
    else:
        f.template_name = request.template_prefix + "/flatpages/default.html"
    return render_flatpage(request, f)

