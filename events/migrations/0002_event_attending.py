# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-11 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_person_events'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attending',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='register.Person'),
            preserve_default=False,
        ),
    ]
