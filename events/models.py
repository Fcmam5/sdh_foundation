# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()
    place = models.CharField(max_length = 120, default = 'جامعة وهران1 أحمد بن بلة')
    timing = models.DateField(auto_now = False, auto_now_add = False)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    created = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.title

    def __unicode__(self): 
        return smart_unicode(self.title)