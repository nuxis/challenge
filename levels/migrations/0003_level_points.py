# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_level_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='points',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
