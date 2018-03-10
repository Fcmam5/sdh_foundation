# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.utils.encoding import smart_unicode
from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from django.utils.translation import ugettext_lazy as _

# Create your models here.
def upload_posters_location(instance, filename):
        title = instance.title
        return "events/event%s/%s" %(instance.id, filename)

class Event(models.Model):
    title = models.CharField(max_length = 120)
    is_active = models.BooleanField(default=True, blank=False)
    content = models.TextField()
    poster = models.ImageField(upload_to = upload_posters_location, verbose_name='Poster', default='default.jpg')
    place = models.CharField(max_length = 120, default = 'جامعة وهران1 أحمد بن بلة')
    timing = models.DateField(_("Due date"),auto_now = False, auto_now_add = False)
    updated = models.DateTimeField(_("Last update"), auto_now = True, auto_now_add = False)
    created = models.DateTimeField(auto_now = False, auto_now_add = True)
    location = PlainLocationField(based_fields=['city'], zoom=0, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event", kwargs={"id" : self.id})

    def get_location(self):
        geoposition = {
            'long': float(self.location.split(',')[0]),
            'latt': float(self.location.split(',')[1])
        }
        return geoposition

    def is_event_active(self):
        return self.is_active and self.timing >= timezone.now().date()

    class Meta:
        verbose_name_plural = _('events')
        verbose_name = _('event')
