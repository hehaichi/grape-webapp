# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-11 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20161011_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='id',
            new_name='identity',
        ),
    ]
