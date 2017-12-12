# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0010_auto_20171206_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weathersuggestion',
            name='clothing',
        ),
        migrations.AddField(
            model_name='weathersuggestion',
            name='clothing_types',
            field=models.ManyToManyField(help_text='Select the clothing types to be worn for this type of weather', to='mycloset.ClothingType'),
        ),
    ]