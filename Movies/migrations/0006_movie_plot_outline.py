# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 18:35


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_remove_movie_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Plot_outline',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
