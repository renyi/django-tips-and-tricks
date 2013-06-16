# models.py

from django.db import models
from django.views.generic.base import TemplateResponseMixin


class CrudUrl(models.Model):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        self._objname = self._meta.object_name.lower()
        super(CrudUrl, self).__init__(*args, **kwargs)

    @models.permalink
    def get_list_url(self):
        return ('%s_list' % self._objname, None, {})

    @models.permalink
    def get_absolute_url(self):
        return ('%s_details' % self._objname, None, {'slug': self.slug})

    @models.permalink
    def get_create_url(self):
        return ('%s_create' % self._objname, None, {})

    @models.permalink
    def get_update_url(self):
        return ('%s_update' % self._objname, None, {'slug': self.slug})

    @models.permalink
    def get_delete_url(self):
        return ('%s_delete' % self._objname, None, {'slug': self.slug})


class Slugged(models.Model):
    title = models.CharField(_("Title"), max_length=500)
    slug = models.CharField(_("URL"), max_length=2000)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Create a unique slug by appending an index.
        """
        pass

    def get_slug(self):
        """
        Allows subclasses to implement their own slug creation logic.
        """
        return slugify(self.title)


class School(Slugged, CrudUrl, FilterMixin):
    pass
