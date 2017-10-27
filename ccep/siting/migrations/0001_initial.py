# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-20 04:36
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='County Name')),
                ('geoid', models.TextField(verbose_name='County Name')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
