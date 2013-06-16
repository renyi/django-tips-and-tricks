# urls.py

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    ('', include("default_app.urls")),
    ('', include("mezzanine.urls")),
)
