# Django settings
SECRETKEY = '7@ug(w91q62^z^vf3fcs$95+@&18m8vj#+of03q5#058axfd_8'
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
