# Generated by Django 4.1.4 on 2022-12-23 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_merge_20221223_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='count_views',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]
