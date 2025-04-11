# movie/views.py
from rest_framework import viewsets
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
