import os
import dj_database_url

from .base import *


ALLOWED_HOSTS = ['schoolms-backend.herokuapp.com']

INSTALLED_APPS += []

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
