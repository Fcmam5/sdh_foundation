# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-02 20:35
from __future__ import unicode_literals

import articles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20170901_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'verbose_name': 'categorie', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Posted'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=articles.models.upload_location),
        ),
    ]