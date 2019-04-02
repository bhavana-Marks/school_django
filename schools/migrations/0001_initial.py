# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(default='default', max_length=250)),
                ('LastName', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
                ('PhoneNumber', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=250)),
                ('Dob', models.CharField(max_length=250)),
                ('Gender', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=250)),
                ('ZipCode', models.CharField(max_length=250)),
                ('Country', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=250)),
            ],
        ),
    ]
