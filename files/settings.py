# settings.py

from .default_settings import *

# Insers default theme app
INSTALLED_APPS.insert(1, "my_project.themes.default")

# Removes CSRF checking
if "django.middleware.csrf.CsrfViewMiddleware" in MIDDLEWARE_CLASSES:
    MIDDLEWARE_CLASSES.remove("django.middleware.csrf.CsrfViewMiddleware")

# LOCAL SETTINGS #
try:
    from local_settings import *
except ImportError:
    pass

# DYNAMIC SETTINGS #
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())