# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_auto_20180530_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areas',
            name='area_Name',
        ),
        migrations.DeleteModel(
            name='Areas',
        ),
    ]