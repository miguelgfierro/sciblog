from django import template
import sciblog.settings as scisettings

register = template.Library()

"""
    Returns data from Google Analytics defined in settings.py

    To load in the template:
    {% load analytics %}
    ...
    <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

        ga('create', '{% ga_tracking_id %}', 'auto');
        ga('send', 'pageview');
    </script>
"""

@register.simple_tag
def ga_tracking_id():
    return scisettings.GA_TRACKING_ID