import urlparse
from django import template
register = template.Library()

@register.filter(name='youtube_embed')
def youtube_embed(url):
    url_data = urlparse.urlparse(url)
    query = urlparse.parse_qs(url_data.query)
    try:
        video_id = query["v"][0]
        print 'video_id=',video_id
        embed_url = 'http://youtube.com/embed/%s' % video_id
        return embed_url
    except KeyError:
        print 'ERROR in embeding video ',url
    return ''
