# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='year1',
            field=models.IntegerField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='year2',
            field=models.IntegerField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='year3',
            field=models.IntegerField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='year4',
            field=models.IntegerField(blank=True, max_length=10),
        ),
    ]
