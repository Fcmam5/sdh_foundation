# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-28 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'images'},
        ),
    ]