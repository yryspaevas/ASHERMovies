from rest_framework.viewsets import ModelViewSet
from review.models import Like

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, action
from django.db.models import Q
from rest_framework.response import Response

from .serializers import CountrySerializer, GenreSerializer, MovieSerializer
from .models import Country, Genre, Movie
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from rest_framework import filters

from review.models import Favourite
from checkaccount.models import User

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    def get_permissions(self):
        if self.action in ['retrive', 'list', 'search']:
            return []
        return [IsAdminUser()]

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    def get_permissions(self):
        if self.action in ['retrive', 'list', 'search']:
            return []
        return [IsAdminUser()]
        

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def get_permissions(self):
        if self.action in ['retrive', 'list', 'search']:
            return []
        return [IsAdminUser()]
    filter_backends = [
        filters.OrderingFilter, 
        filters.SearchFilter, 
    ]
    filterset_fields = ['title', 'year',]
    search_fields = ['title', 'year',]
    ordering_fields = ['title', 'year', 'average_rating']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() # Product.objects.all()
        if q:
            queryset = queryset.filter(Q(title__icontains=q))

        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    
    # @action(['POST'], detail=False)
    # def like_or_dislike(self, request):
    #     movie_id = request.POST.get('id')
    #     action = request.POST.get('action')
    #     if movie_id and action:
    #         try:
    #             movie = Movie.objects.get(id=movie_id)
    #             if action == 'like':
    #                 # movie.movie_like.add(request.user)
    #                 Like.objects.create()
    #             else:
    #                 # movie.post_like.remove(request.user)
    #                 Like.objects.delete()
    #             if action == 'dislike':
    #                 movie.movie_dislike.add(request.user)
    #             else:
    #                 movie.post_dislike.remove(request.user)
    #                 return Response(status=201)
    #         except:
    #             pass
    #     return Response(status=201)


    # @action(['POST'], detail=False)
    # def user_like(self, request):
    #     likes = Like.objects.all()
    #     for like in likes:
    #         if like.like_or_dislike == "like":
    #             like.for_movie.movie_like.add(like.user)
    #         if like.like_or_dislike == "dislike":
    #             like.for_movie.movie_dislike.add(like.user)
    #     return Response("Complete")

 

# def movie_detail(request, slug):

#     # Проверяем есть ли пост с запрашиваемым слагом
#     movie = get_object_or_404(Movie, slug__iexact=slug)
#     if not request.session.session_key:
#         request.session.save()
#     # получаем сессию
#     session_key = request.session.session_key

#     is_views = MovieCountViews.objects.filter(movieId=movie.id, sesId=session_key)

#     # если нет информации о просмотрах создаем ее
#     if is_views.count() == 0 and str(session_key) != 'None':

#         views = MovieCountViews()
#         views.sesId = session_key
#         views.movieId = movie
#         views.save()

#         movie.count_views += 1
#         movie.save()

#     return render(request, 'post_detail.html', context={'post': post})