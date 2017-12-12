# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0005_auto_20171202_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='weathertype',
            name='clothing_types',
            field=models.ManyToManyField(help_text='Select clothing types to be simultaneously worn in this weather', to='mycloset.ClothingType'),
        ),
    ]
