# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_remove_userinfo_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='PhoneNumber',
            field=models.IntegerField(),
        ),
    ]
