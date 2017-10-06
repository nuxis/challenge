# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0008_level_required_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='is_external',
            field=models.BooleanField(default=False, help_text='Check answer against URL in answer field'),
        ),
        migrations.AlterField(
            model_name='level',
            name='answer',
            field=models.CharField(help_text='Answer here. If multianswer, split with "||". If external, URL here.', max_length=256),
        ),
    ]