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
    except:
        print 'ERROR: Problem when accessing object'
        return ""

    return current_site.domain
