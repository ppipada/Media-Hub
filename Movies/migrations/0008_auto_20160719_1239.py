# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 12:39


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0007_auto_20160717_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='is_favorite',
            new_name='Watched',
        ),
    ]
