# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20180530_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1),
        ),
        migrations.AddField(
            model_name='areas',
            name='area_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.City'),
        ),
    ]
