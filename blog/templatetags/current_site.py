from django import template
from django.contrib.sites.models import Site
register = template.Library()

@register.simple_tag
def current_site():
    """
        Returns the url for the current site defined by SITE_ID in sciblog/settings.py
    """
    try:
        current_site = Site.objects.get_current()
        print 'site=', current_site.domain
    except:
        return "Problem when accessing object"

    return current_site.domain
