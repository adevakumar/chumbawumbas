# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0014_auto_20171030_1730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]