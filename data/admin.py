# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import SEF_data, Slogo
from users.models import CustomUser


# Register your models here.

# Customize my admin
class SEFModelAdmin(admin.ModelAdmin):
    list_display = ["id"] 
    class Meta:
        model = SEF_data

class SlogoModelAdmin(admin.ModelAdmin):
    list_display = ["id", ] 
    class Meta:
        model = Slogo


admin.site.register(SEF_data, SEFModelAdmin)
admin.site.register(Slogo, SlogoModelAdmin)

