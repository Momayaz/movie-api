from django.shortcuts import render
from rest_framework import viewsets
from .models import MoviesData
from .serializer import Serilaizer_Movie
# Create your views here.

class View_Serializer(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = Serilaizer_Movie

class Action_Serializer(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='action')
    serializer_class = Serilaizer_Movie

class Comedy_Serializer(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='comedy')
    serializer_class = Serilaizer_Movie