from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_movie_movie_dislike_remove_movie_movie_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(blank=True, to='main.genre'),
            # field=models.CharField(blank=True, choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'drama'), ('FANTASY', 'Fantasy'), ('HORROR', 'Horror'), ('MUSICALS', 'Musicals'), ('MYSTERY', 'Mystery'), ('ROMANCE', 'Romance'), ('THRILLER', 'Thriller'), ('WESTERN', 'Western')], max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default=0, help_text='указывать сумму в долларах'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_year',
            field=models.IntegerField(default=0),
        ),
    ]
