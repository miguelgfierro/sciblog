"""
Django settings for sciblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import socket
from sciblog.private import SECRETKEY, DEBUG_FLAG, DISQUS_KEY


def get_ip():
    """Returns the current IP

    Returns:
        str: IP
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


CURRENT_IP = get_ip()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETKEY

# Set DEBUG = False in production. Set DEBUG = True in localhost development
# This flag is set in an external file private.py
DEBUG = DEBUG_FLAG

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "www.miguelgfierro.com",
    "miguelgfierro.com",
    CURRENT_IP,
]

# Application definition
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django.contrib.syndication",
    "django.contrib.sitemaps",
    "libs.django-disqus.disqus",  # for comments
    "libs.ckeditor",  # for managing text,images and formulas
    "libs.ckeditor_uploader",
)
SITE_ID = 1

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "blog.middleware.MobileTemplatesMiddleware",
)

# Template directory
MOBILE_TEMPLATE_PREFIX = "mobile"
DESKTOP_TEMPLATE_PREFIX = "desktop"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here (templates are defined at runtime)
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
            ],
        },
    },
]

# list of IPs able to see the toolbar
INTERNAL_IPS = (
    "127.0.0.1",
    "localhost",
)

# URLs and WSGI
ROOT_URLCONF = "sciblog.urls"
WSGI_APPLICATION = "sciblog.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "img")
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/img/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "blog", "static"),)

# Number of posts per page in the list view
POSTS_PER_PAGE = 10 

# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "django.log"),
            "maxBytes": 15728640,  # 1024*1024*15 = 15MB
            "backupCount": 10,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# Http protocol with (https://) or without SSL (http://)
# NOTE: You need to have a SSL certificate installed before setting this flag
# to True
HTTPS = True

# Ckeditor
CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_IMAGE_BACKEND = "pillow"

# ---------------- IMPORTANT NOTE ----------------
# CHANGE THE FOLLOWING SETTINGS WITH YOUR OWN DATA
# ------------------------------------------------

# Social Networks
FACEBOOK_PIXEL = "2573724289540878"  # for Facebook tracking
FACEBOOK_URL = ""
TWITTER_URL = "https://twitter.com/miguelgfierro"
TWITTER_HANDLE = "miguelgfierro"
LINKEDIN_URL = "https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=miguelgfierro"
LINKEDIN_PARTNER_ID = "3247881"  # for Linkedin Insight Tag
PINTEREST_URL = ""
INSTAGRAM_URL = ""
YOUTUBE_URL = ""
RSS_URL = "https://feeds.feedburner.com/miguelgfierro"
NEWSLETTER_URL = "https://miguelgfierro.com/sendy/subscription?f=22QIIP0tF8Bx5qYtjCFQa5NDaXYeyG8FyFs40uOzc7LGvlTMGG3Dx2fOogECvG2rMYrUAi3UPtV8927JF18Qhw892A"
GITHUB_URL = "https://github.com/miguelgfierro"
EMAIL_ADDRESS = "info@miguelgfierro.com"

# Analytics
GA_TRACKING_ID = "GTM-T8DSN55"

# Disqus configuration (for managing comments)
# To install disqus http://django-disqus.readthedocs.org/en/latest/index.html
DISQUS_API_KEY = DISQUS_KEY
DISQUS_WEBSITE_SHORTNAME = "miguelgfierro"
