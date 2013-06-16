# default_settings.py

DEBUG = False
TEMPLATE_DEBUG = False
USE_SOUTH = True
ADMINS = [('Devtune Admin', 'admin@devtune.biz')]
MANAGERS = ADMINS
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = "en-gb"
USE_TZ = True
TIME_ZONE = 'Asia/Kuala_Lumpur'
INTERNAL_IPS = ["127.0.0.1"]
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SITE_ID = 1
STATIC_URL = '/static/'
MEDIA_URL = '/media'
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "compressor",
]
