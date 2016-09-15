from django.shortcuts import render
from rest_framework.views import APIView
from rutas.models import Ruta
from rest_framework import generics
from sitios.serializers import RutaSerializer

class RutaCreate(generics.CreateAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

class RutaList(generics.ListAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
