# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_auto_20161216_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='img_url',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
