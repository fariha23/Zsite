# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_auto_20161220_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='art',
            name='description',
            field=models.CharField(default='Write something about your art!!', max_length=500),
        ),
    ]
