# Generated by Django 4.1.4 on 2022-12-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_movie_genre_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='count_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]