# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='medium',
            field=models.CharField(default='Pencils', max_length=50),
        ),
    ]