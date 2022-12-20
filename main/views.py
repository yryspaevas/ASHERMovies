from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

from .serializers import CountrySerializer, GenreSerializer, MovieSerializer
from .models import Country, Genre, Movie

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    