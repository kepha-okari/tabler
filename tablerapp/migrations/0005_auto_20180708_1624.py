# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablerapp', '0004_unit_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]