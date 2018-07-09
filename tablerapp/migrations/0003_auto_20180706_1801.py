# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-06 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablerapp', '0002_auto_20180622_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='lecturer',
            name='unit',
            field=models.ManyToManyField(to='tablerapp.Unit'),
        ),
    ]
