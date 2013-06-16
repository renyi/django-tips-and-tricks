# urls.py

from django.conf.urls import patterns, include, url
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import School


urlpatterns = patterns('',
    url(r'^school/$',
       ListView.as_view(),
       name="school_list"),

    url(r'^school/add/$',
       CreateView.as_view(),
       name="school_create"),

    url(r'^school/update/(?P<slug>.*)/$',
       UpdateView.as_view(),
       name="school_update"),

    url(r'^school/delete/(?P<slug>.*)/$',
       DeleteView.as_view(),
       name="school_delete"),

    url(r'^school/(?P<slug>.*)/$',
       DetailView.as_view(),
       name="school_details"),
)
