# views.py

from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import School


class FilterMixin(object):
    allowed_filters = {}

    def get_queryset_filters(self):
        filters = {}

        for item in self.request.GET:
            allowed = self.allowed_filters.get(item)
            if allowed:
                keyname = "%s" % allowed
                filter_values = self.request.GET.getlist(item)
                filters[keyname] = filter_values
        return filters

    def get_queryset(self):
        qs = super(FilterMixin, self).get_queryset()
        return qs.filter(**self.get_queryset_filters())


class AjaxTemplateResponseMixin(TemplateResponseMixin):
    def get_template_names(self):
        """
        Return a list of template names to be used for the request.
        """
        try:
            names = super(AjaxTemplateResponseMixin, self).get_template_names()
        except ImproperlyConfigured:
            names = []

        try:
            opts = self.form_class._meta.model._meta
        except:
            try:
                opts = self.object_list.model._meta
            except:
                try:
                    opts = self.object._meta
                except:
                    opts = None

        if opts:
            opts_list = (opts.app_label, opts.object_name.lower(), self.template_name_suffix)

            if self.request.is_ajax():
                name = "%s/includes/%s%s.html" % opts_list

            else:
                name = "%s/%s%s.html" % opts_list

            names.append(name)

        return names


class SchoolListView(ListView, FilterMixin, AjaxTemplateResponseMixin):
    '''
    Template: school/school_list.html
    AJAX Template: school/includes/school_list.html
    '''
    model = School
    allowed_filters = {
        'title': 'title__icontains',
        'slug': 'slug__icontains',
    }


class SchoolDetailView(DetailView, AjaxTemplateResponseMixin):
    '''
    Template: school/school_detail.html
    AJAX Template: school/includes/school_detail.html
    '''
    model = School


class SchoolCreateView(CreateView, AjaxTemplateResponseMixin):
    '''
    Template: school/school_form.html
    AJAX Template: school/includes/school_form.html
    '''
    model = School


class SchoolUpdateView(UpdateView, AjaxTemplateResponseMixin):
    '''
    Template: school/school_form.html
    AJAX Template: school/includes/school_form.html
    '''
    model = School


class SchoolDeleteView(DeleteView, AjaxTemplateResponseMixin):
    '''
    Template: school/school_confirm_delete.html
    AJAX Template: school/includes/school_confirm_delete.html
    '''
    model = School
