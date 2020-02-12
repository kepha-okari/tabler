# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tablerapp', '0007_auto_20180708_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='unit',
        ),
        migrations.AddField(
            model_name='unit',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assign',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablerapp.Lecturer'),
        ),
        migrations.AddField(
            model_name='assign',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablerapp.Unit'),
        ),
    ]