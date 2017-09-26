# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20161007_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='webhook_admins',
            field=models.CharField(default=None, help_text='Slack-compatible webhooks for admins. May contain game-sensitive information', max_length=512, null=True),
        ),
    ]