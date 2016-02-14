from django import template
from django.contrib.sites.models import Site
import sciblog.settings as scisettings

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

@register.simple_tag
def http_or_https():
    """
        Returns the http protocol. By default the protocol is http:// but if it's defined in settings, the protocol
        can be https://
    """
    if scisettings.HTTPS and not scisettings.DEBUG:
        return 'https://'
    else:
        return 'http://'