# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0017_auto_20171030_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='clothing_image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
