# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from location_field.models.plain import PlainLocationField



# Create your models here.
def upload_location(instance, filename):
    title = instance.slogo.foundation_name
    slug =  slugify(title)
    return "sponsors/sponsor%s/%s" %(instance.slogo, filename)

def upload_locationlogo(instance, filename):
    title = instance.logo
    slug =  slugify(title)
    return "logos/%s" % (filename)


# ALL information about the foundation
class SEF_data(models.Model):
    foundation_name = models.CharField(_('Title'),max_length=100, db_index=True)
    slug = models.SlugField(_('Slug'),max_length=100, unique=True, db_index=True)
    logo = models.ImageField(upload_to = upload_locationlogo)
    description = models.TextField()
    privacy = models.TextField()
    policy = models.TextField()
    foundation_gmail = models.CharField(_('Email'),max_length=100)
    foundation_phone = models.CharField(_('Phone'),max_length=100)
    foundation_address = models.CharField(_('Address'),max_length=100)
    foundation_location = PlainLocationField(based_fields=['city'], zoom=0, blank=True, null=True)

    def __str__(self):
        return self.foundation_name

    def get_absolute_url(self):
        return reverse("foundation", kwargs={"id" : self.id})

    class Meta:
        verbose_name_plural = _('Foundation_datas')
        verbose_name = _('Foundation_data')

class Slogo(models.Model):
    image = models.ImageField(upload_to = upload_location)
    alt_text = models.CharField(_('Image description'),max_length=100,
        help_text=_('Descripe your image, this field is important to search engines and for web accessibility'))
    slogo = models.ForeignKey(SEF_data, default = None)

    class Meta:
        verbose_name_plural = _('Sponsors')
        verbose_name = _('Sponsor')