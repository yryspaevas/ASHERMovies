from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CommentSerializer, FavouriteSerializer, RatingSerializer
from .models import Comment, Favourite,Rating, Like

from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from account.models import User
from main.models import Movie

class CommetViewSet(ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer


class CreateRatingAPIView(APIView):
    def post(self, request):
        user = request.user
        serializer = RatingSerializer(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        movie_id = request.data.get("movie")
        if Rating.objects.filter(user=user, movie__id=movie_id).exists():
            rating = Rating.objects.get(user=user, movie__id=movie_id)
            rating.value = request.data.get("value")
            rating.save()
        else:
            serializer.save()
        return Response(status=201)

@api_view(['POST'])
def favourite(request):
    user_id = request.data.get('user')
    movie_id = request.data.get('movie')
    user = get_object_or_404(User, id=user_id)
    movie = get_object_or_404(Movie, id = movie_id)

    if Favourite.objects.filter(user=user, movie=movie).exists():
        Favourite.objects.filter(user=user, movie=movie).delete()
    else:
        Favourite.objects.create(movie=movie, user=user)
    return Response(status=201)


@api_view(['POST'])
def like_or_dislike(request):
    movie_id = request.POST.get('id')
    action = request.POST.get('action')
    if movie_id and action:
        try:
            movie = Movie.objects.get(id=movie_id)
            if action == 'like':
                movie.movie_like.add(request.user)
            else:
                movie.post_like.remove(request.user)
            if action == 'dislike':
                movie.movie_dislike.add(request.user)
            else:
                movie.post_dislike.remove(request.user)
                return Response(status=201)
        except:
            pass
    return Response(status=201)


@api_view(['POST'])
def user_like(request):
    likes = Like.objects.all()
    for like in likes:
        if like.like_or_dislike == "like":
            like.for_movie.movie_like.add(like.user)
        if like.like_or_dislike == "dislike":
            like.for_movie.movie_dislike.add(like.user)
    return Response("Complete")