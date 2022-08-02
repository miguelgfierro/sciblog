from django import template
import sciblog.settings as scisettings

register = template.Library()


@register.simple_tag
def ga_tracking_id():
    """
    Returns data from Google Tag Manager defined in settings.py.

    For more information about Google Tag Manager, see https://tagmanager.google.com/

    To load in the template, add in the header:
    {% load analytics %}
    ...
    <!-- Google Tag Manager -->
    <script>
    (function (w, d, s, l, i) {
      w[l] = w[l] || []; w[l].push({
        'gtm.start':
          new Date().getTime(), event: 'gtm.js'
      }); var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
          'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', '{% ga_tracking_id %}');
    </script>
    <!-- End Google Tag Manager -->

    Then add in the body:
    <!-- Google Tag Manager (noscript) -->
    <noscript>
    <iframe src="https://www.googletagmanager.com/ns.html?id={% ga_tracking_id %}" height="0" width="0"
        style="display:none;visibility:hidden">
    </iframe>
    </noscript>
    <!-- End Google Tag Manager (noscript) -->

    """
    return scisettings.GA_TRACKING_ID
