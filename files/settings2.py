# settings.py

import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

# User project directory name as default "theme" app
INSTALLED_APPS.insert(1, "%s" % PROJECT_DIRNAME)

ROOT_URLCONF = '%s.urls' % PROJECT_DIRNAME
CACHE_MIDDLEWARE_KEY_PREFIX = '%s' % PROJECT_DIRNAME
CACHE_MIDDLEWARE_ALIAS = '%s' % PROJECT_DIRNAME
CSRF_COOKIE_NAME = '%s_csrftoken' % PROJECT_DIRNAME
LANGUAGE_COOKIE_NAME = '%s_language' % PROJECT_DIRNAME
SESSION_COOKIE_NAME = '%s_session' % PROJECT_DIRNAME
STATIC_ROOT = '/static/%s/' % PROJECT_DIRNAME
MEDIA_ROOT = '/media/%s/' % PROJECT_DIRNAME
WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_DIRNAME

# Celery
BROKER_VHOST = PROJECT_DIRNAME
BROKER_URL = '%s%s' % (BROKER_URL, BROKER_VHOST)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "%s" % PROJECT_DIRNAME,
        "HOST": "127.0.0.1",
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': ['127.0.0.1:11211'],
        'KEY_PREFIX': '%s' % PROJECT_DIRNAME,
    }
}
