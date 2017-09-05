# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-02 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.AlterField(
            model_name='event',
            name='timing',
            field=models.DateField(verbose_name='Due date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last update'),
        ),
    ]