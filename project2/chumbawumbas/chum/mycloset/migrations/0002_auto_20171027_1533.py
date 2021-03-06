# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycloset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
            ],
        ),
        migrations.RenameModel(
            old_name='Genre',
            new_name='Outfit',
        ),
        migrations.RenameModel(
            old_name='Author',
            new_name='Weather',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.AddField(
            model_name='clothing',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mycloset.Weather'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='genre',
            field=models.ManyToManyField(help_text='Select an outfit for this book', to='mycloset.Outfit'),
        ),
    ]
