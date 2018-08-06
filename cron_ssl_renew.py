import requests
import json
from sciblog.private import CLOUDFLARE_ZONEID, CLOUDFLARE_APIKEY
from sciblog.settings import EMAIL_ADDRESS


# Variables
HEADERS = {
    'Content-type': 'application/json',
    'X-Auth-Email': EMAIL_ADDRESS,
    'X-Auth-Key': CLOUDFLARE_APIKEY
}

ENDPOINT = 'https://api.cloudflare.com/client/v4/zones/' + CLOUDFLARE_ZONEID


def pause_cloudflare():
    data = {'paused': 'true'}
    res = requests.patch(ENDPOINT,
                         data=json.dumps(data), headers=HEADERS)
    if res.ok:
        print("Cloudflare paused")
    else:
        print("ERROR when pausing Cloudflare")
        print(res.json())


def resume_cloudflare():
    data = {'paused': 'false'}
    res = requests.patch(ENDPOINT,
                         data=json.dumps(data), headers=HEADERS)
    if res.ok:
        print("Cloudflare resumed")
    else:
        print("ERROR when resuming Cloudflare")
        print(res.json())


# pause_cloudflare()
resume_cloudflare()
