# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 20:15


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0006_movie_plot_outline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Imdb_rating',
            field=models.FloatField(default=0.0),
        ),
    ]
