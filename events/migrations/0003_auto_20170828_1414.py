# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-28 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170828_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(default='default.jpg', upload_to=events.models.upload_posters_location, verbose_name='Poster'),
        ),
    ]
