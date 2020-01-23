# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-01-10 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0004_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]