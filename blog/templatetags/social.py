from django import template

import sciblog.settings as scisettings


register = template.Library()


"""
    Returns data from social networks defined in settings.py

    To load in the template:
    {% load social %}
    ...
    <a href="{% facebook_url %}">Link to Facebook</a>
"""

@register.simple_tag
def facebook_url():
    return scisettings.FACEBOOK_URL


@register.simple_tag
def facebook_pixel():
    return scisettings.FACEBOOK_PIXEL


@register.simple_tag
def twitter_url():
    return scisettings.TWITTER_URL


@register.simple_tag
def twitter_handle():
    return scisettings.TWITTER_HANDLE


@register.simple_tag
def linkedin_url():
    return scisettings.LINKEDIN_URL


@register.simple_tag
def linkedin_partner_id():
    return scisettings.LINKEDIN_PARTNER_ID


@register.simple_tag
def pinterest_url():
    return scisettings.PINTEREST_URL


@register.simple_tag
def instagram_url():
    return scisettings.INSTAGRAM_URL


@register.simple_tag
def youtube_url():
    return scisettings.YOUTUBE_URL


@register.simple_tag
def tiktok_url():
    return scisettings.TIKTOK_URL


@register.simple_tag
def tiktok_pixel():
    return scisettings.TIKTOK_PIXEL


@register.simple_tag
def rss_url():
    return scisettings.RSS_URL


@register.simple_tag
def github_url():
    return scisettings.GITHUB_URL


@register.simple_tag
def email_address():
    return scisettings.EMAIL_ADDRESS


@register.simple_tag
def newsletter_url():
    return scisettings.NEWSLETTER_URL
