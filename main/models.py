from django.db import models
from account.models import User

# GENRE = [
#     ('ACTION', 'Action'),
#     ('ADVENTURE', 'Adventure'),
#     ('COMEDY', 'Comedy'),
#     ('DRAMA', 'drama'),
#     ('FANTASY', 'Fantasy'),
#     ('HORROR', 'Horror'),
#     ('MUSICALS', 'Musicals'),
#     ('MYSTERY', 'Mystery'),
#     ('ROMANCE', 'Romance'),
#     ('THRILLER', 'Thriller'),
#     ('WESTERN', 'Western')
# ]

class Genre(models.Model):
    title = models.CharField(max_length=25)

    def ____str____(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    
class Country(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Movie(models.Model):
    # genre = models.CharField(choices=GENRE, max_length=100 , blank=True)
    country = models.ForeignKey(Country, related_name='country_movie', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.PositiveBigIntegerField(default=0, help_text="указывать сумму в долларах")
    created_year = models.PositiveSmallIntegerField(default=2019)
    image = models.ImageField(upload_to='media', null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
    
