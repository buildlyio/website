from .base import *
import os
from os.path import join, normpath

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'buildly-cms',
        'PASSWORD': os.environ.get("PASSWORD"),
        'USER': 'buildly-cms',
        'HOST': 'db-mysql-nyc3-97229-do-user-2508039-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['ob-cms-dwtkh.ondigitalocean.app', 'buildly.io', '127.0.0.1', '[::1]','www.buildly.io',]

try:
    from .local import *
except ImportError:
    pass
