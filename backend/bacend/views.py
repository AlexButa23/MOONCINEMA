from django.shortcuts import render
from .models import *
from django.core import serializers
from .serializers import *
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
class filmeViewSet (ModelViewSet):
    queryset=film.objects.all()
    serializer_class=filmeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gen','nume']
class rezervareViewSet (ModelViewSet):
    queryset=rezervare.objects.all()
    serializer_class=rezervareSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['film']
class recomandariViewSet (ModelViewSet):
    queryset=recomandari.objects.all()
    serializer_class=recomandariSerializer


# Create your views here.
