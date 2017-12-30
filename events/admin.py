# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event
# Register your models here.

# Customize my admin
class EventModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated", "timing","is_active"] 
    class Meta:
        model = Event


admin.site.register(Event, EventModelAdmin)
