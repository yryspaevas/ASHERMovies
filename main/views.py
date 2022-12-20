from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, action
from django.db.models import Q
from rest_framework.response import Response

from .serializers import CountrySerializer, GenreSerializer, MovieSerializer
from .models import Country, Genre, Movie
from rest_framework.permissions import IsAdminUser

from rest_framework import filters

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [
        filters.OrderingFilter, 
        filters.SearchFilter, 
    ]
    filterset_fields = ['title', 'year',]
    search_fields = ['title', 'year',]
    ordering_fields = ['title', 'year', 'average_rating']

@api_view(['GET'])
def toggle_like(request, m_id):
    user = request.user
    movie = get_object_or_404(Movie, id=m_id)

    # if Like.objects.filter(user=user, movie=movie).exists():
    #     Like.objects.filter(user=user, movie=movie).delete()
    # else:
    #     Like.objects.create(user=user, movie=movie)
    # return Response("Like toggled", 200)

    # @action(['GET'], detail=False)
    # def search(self, request):
    #     q = request.query_params.get('q')

    #     if q:
    #         queryset = queryset.filter(Q(title__icontains=q) | Q(author__first_name__icontains=q) | Q(author__last_name__icontains=q))

    #     pagination = self.paginate_queryset(queryset)
    #     if pagination:
    #         serializer = self.get_serializer(pagination, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data, status=200)