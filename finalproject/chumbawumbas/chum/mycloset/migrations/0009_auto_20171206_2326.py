# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0008_weather_weather_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing', models.ManyToManyField(help_text='Select the clothing to be worn for this type of weather', to='mycloset.Clothing')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='maximum_cold_temperature',
            field=models.IntegerField(default='5', help_text='Please enter the maximum temperature (Celsius) that you would consider cold. Temperatures above this are cool, then warm, then hot.', max_length=3),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='maximum_cool_temperature',
            field=models.IntegerField(default='16', help_text='Please enter the maximum temperature (Celsius) that you would consider cool. Temperatures above this are warm, then hot.', max_length=3),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='maximum_warm_temperature',
            field=models.IntegerField(default='27', help_text='Please enter the maximum temperature (Celsius) that you would consider warm. Temperatures above this are hot.', max_length=3),
        ),
    ]
