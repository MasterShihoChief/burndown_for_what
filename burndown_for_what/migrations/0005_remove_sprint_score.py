# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-05 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burndown_for_what', '0004_issue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='score',
        ),
    ]