# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0019_remove_clothing_clothing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='clothing_picture',
            field=models.ImageField(null=True, upload_to='clothing_pictures/'),
        ),
    ]
