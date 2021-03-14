# Private template script
# To enable this script just rename it to private.py
# $ cp sciblog/private.template.py sciblog/private.py

# Django settings
SECRETKEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
DEBUG_FLAG = False

# Cloudflare settings (optional)
# The ZoneID can be obtained in the main dashboard under domain summary
# The API Key can be accessed in the profile https://dash.cloudflare.com/profile
# If you are using Cloudflare, set CLOUDFLARE_FLAG to True
CLOUDFLARE_FLAG = False
CLOUDFLARE_ZONEID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CLOUDFLARE_APIKEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Let's Encript certbot path (optional)
# $ wget https://dl.eff.org/certbot-auto
CERTBOT_AUTO_PATH = '/path/to/certbot-auto'

# Disqus API key
DISQUS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'


