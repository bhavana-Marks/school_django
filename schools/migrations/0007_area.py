# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-31 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_auto_20180530_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_areas', models.CharField(max_length=250)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.City')),
            ],
        ),
    ]
