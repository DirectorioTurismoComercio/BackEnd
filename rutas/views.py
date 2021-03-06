from django.shortcuts import render
from rest_framework.views import APIView
from rutas.models import Ruta, RutaSitio
from rest_framework import generics
from sitios.serializers import RutaSerializer
from rest_framework import status
from rest_framework.response import Response
from rutas.permissions import IsRouteOwner
from rest_framework.permissions import IsAuthenticated
from translator import  translator


class RutaCreate(generics.CreateAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    permission_classes = (IsAuthenticated,)
    def create(self, request):
		data = request.data
		traductor = translator.Translator()

		serializer = RutaSerializer(data=data)
		if serializer.is_valid():
			newObject = serializer.save()
			newObject.description = traductor.getTranslatedWord(newObject.descripcion)
			newObject.save()

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
    permission_classes = (IsAuthenticated, IsRouteOwner)

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

    def perform_update(self, serializer):
		instance = serializer.save()
		traductor = translator.Translator()
		instance.description = traductor.getTranslatedWord(instance.descripcion)
		instance.save()
