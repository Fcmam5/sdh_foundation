# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-30 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20171230_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sef_data',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sef_data',
            name='policy',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sef_data',
            name='privacy',
            field=models.TextField(),
        ),
    ]