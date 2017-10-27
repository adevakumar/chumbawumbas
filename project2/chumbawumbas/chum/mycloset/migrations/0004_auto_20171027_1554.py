# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0003_auto_20171027_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular clothing across whole closet', primary_key=True, serialize=False),
        ),
    ]