# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0004_picture_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='profile_pic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='profiles.Profile'),
        ),
    ]
