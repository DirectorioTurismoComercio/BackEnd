from django.shortcuts import render
from rest_framework.views import APIView
from rutas.models import Ruta
from rest_framework import generics
from sitios.serializers import RutaSerializer
from rest_framework import status
from rest_framework.response import Response

class RutaCreate(generics.CreateAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    def create(self, request):
		data = request.data
		
		serializer = RutaSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			if "sitios" in data:
				sitios = request.data.getlist('sitios')
				serializer.add_sites_to_route(sitios)
		else:
		    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response(status=status.HTTP_201_CREATED)



class RutaList(generics.ListAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    