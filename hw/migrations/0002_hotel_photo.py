# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
