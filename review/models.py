# from django.conf import settings
# from django.contrib.auth import get_user_model
from django.db import models
from account.models import User
from main.models import Movie


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.body[:20]}"


class Favourite(models.Model):
    user = models.ForeignKey(User, related_name='favourite', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name='movie_favourite',  on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} -> {self.movie}'


class Rating(models.Model):
    user = models.ForeignKey(User, related_name='rating', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_rating', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    value = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])

    def __str__(self) -> str:
        return f'{self.user} -> {self.movie}'