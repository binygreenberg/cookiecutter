# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='profiles.Profile'),
        ),
    ]
