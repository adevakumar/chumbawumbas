# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0013_auto_20171030_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.TextField(default='', help_text='Enter your email address', max_length=1000, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone Number'),
        ),
    ]
