# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-25 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('place', models.CharField(default='\u062c\u0627\u0645\u0639\u0629 \u0648\u0647\u0631\u0627\u06461 \u0623\u062d\u0645\u062f \u0628\u0646 \u0628\u0644\u0629', max_length=120)),
                ('timing', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
