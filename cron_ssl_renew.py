import sys
import requests
import json
if sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess
from sciblog.private import (CLOUDFLARE_ZONEID, CLOUDFLARE_APIKEY,
                             CERTBOT_AUTO_PATH)
from sciblog.settings import EMAIL_ADDRESS


# Variables
HEADERS = {
    'Content-type': 'application/json',
    'X-Auth-Email': EMAIL_ADDRESS,
    'X-Auth-Key': CLOUDFLARE_APIKEY
}

ENDPOINT = 'https://api.cloudflare.com/client/v4/zones/' + CLOUDFLARE_ZONEID


def pause_cloudflare():
    """Pause cloudflare. From documentation:
    $ curl -X PATCH "https://api.cloudflare.com/client/v4/zones/0000ZONEID0000" \
           -H "X-Auth-Email: user@example.com" \
           -H "X-Auth-Key: 0000APIKEY0000" \
           -H "Content-Type: application/json" \
           --data '{"paused": true}'
    """
    data = {'paused': True}
    res = requests.patch(ENDPOINT,
                         data=json.dumps(data), headers=HEADERS)
    if res.ok:
        print("Cloudflare paused")
    else:
        print("ERROR when pausing Cloudflare")
        print(res.json())


def resume_cloudflare():
    """Resume cloudflare. From documentation:
    $ curl -X PATCH "https://api.cloudflare.com/client/v4/zones/0000ZONEID0000" \
           -H "X-Auth-Email: user@example.com" \
           -H "X-Auth-Key: 0000APIKEY0000" \
           -H "Content-Type: application/json" \
           --data '{"paused": false}'
    """
    data = {'paused': False}
    res = requests.patch(ENDPOINT,
                         data=json.dumps(data), headers=HEADERS)
    if res.ok:
        print("Cloudflare resumed")
    else:
        print("ERROR when resuming Cloudflare")
        print(res.json())


def renew_ssl_certificate():
    try:
        command = [CERTBOT_AUTO_PATH, "renew", "--quiet",
                   "--keep-until-expiring", "--no-self-upgrade"]
        out_str = subprocess.run(command, stdout=subprocess.PIPE).stdout
        out_str = out_str.decode("utf-8").replace('\r', '')
        print(out_str)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    pause_cloudflare()
    renew_ssl_certificate()
    resume_cloudflare()
