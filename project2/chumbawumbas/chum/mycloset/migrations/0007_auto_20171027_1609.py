# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0006_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular clothing across whole closet', primary_key=True, serialize=False)),
                ('OutfitName', models.CharField(help_text='Enter outfit name', max_length=200)),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('clothing', models.ManyToManyField(help_text='Select all clothing for your outfit', to='mycloset.Clothing')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', help_text='Enter your name', max_length=200),
        ),
    ]
