# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablerapp', '0005_auto_20180708_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='course',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='period',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='room1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='room2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='room3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='room4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='unit1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='unit2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='unit3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='unit4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='year1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='year2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='year3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='year4',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
