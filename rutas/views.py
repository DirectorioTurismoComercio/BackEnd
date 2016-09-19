from django.shortcuts import render
from rest_framework.views import APIView
from rutas.models import Ruta, RutaSitio
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
				serializer.add_sites_to_route(data["sitios"])
		else:
			return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response(status=status.HTTP_201_CREATED)



class RutaList(generics.ListAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    

class RutaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

    def update(self, request, *args, **kwargs):
		data = request.data
		serializer = RutaSerializer(data=data)

		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)


		if serializer.is_valid():
			serializer.save()
			if "sitios" in data:
				RutaSitio.objects.filter(ruta=self.get_object().id).all().delete()
				serializer.add_sites_to_route(data["sitios"])
		else:
			return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response(serializer.data)
