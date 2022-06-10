from django import template
import sciblog.settings as scisettings

register = template.Library()


@register.simple_tag
def ga_tracking_id():
    """
    Returns data from Google Analytics defined in settings.py

    To load in the template:
    {% load analytics %}
    ...
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={% ga_tracking_id %}"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', '{% ga_tracking_id %}');
    </script>
    """
    return scisettings.GA_TRACKING_ID


@register.simple_tag
def sumo_tracking_id():
    """
    Returns data from Sumo defined in settings.py

    To load in the template:
    {% load analytics %}
    ...
    <!-- SUMO Opt-in technology -->
    <script async>
        (function (s, u, m, o, j, v) {
        j = u.createElement(m); v = u.getElementsByTagName(m)[0];
        j.async = 1;
        j.src = o;
        j.dataset.sumoSiteId = '{% sumo_tracking_id %}';
        v.parentNode.insertBefore(j, v)
        })(window, document, 'script', '//load.sumo.com/');
    </script>
    """
    return scisettings.SUMO_TRACKING_ID
