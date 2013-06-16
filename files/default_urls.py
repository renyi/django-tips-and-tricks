# default_urls.py

urlpatterns = patterns('',
    # Default index.html
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),

    # Default favicon
    url(r'^favicon\.ico/$', RedirectView.as_view(url='/static/img/favicon.ico'), name="favicon"),
)

# Default robots.txt
urlpatterns += patterns('',
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt')),
)

# Admin urls
if "django.contrib.admin" in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += patterns("",
        (r"^admin/", include(admin.site.urls)),
    )

# Other apps
if "userena" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        (r'^users/', include('userena.urls')),
    )

if "selectable" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        url(r"^selectable/", include("selectable.urls")),
    )

if "actstream" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        ('^activity/', include('actstream.urls')),
    )
