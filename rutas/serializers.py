from rest_framework import serializers
from rutas.models import Ruta,RutaSitio
from sitios.serializers import SitioSerializer



class RutaSitioSerializer(serializers.ModelSerializer):
	sitio = SitioSerializer(read_only=True) 
	class Meta:
		model = RutaSitio

class RutaSerializer(serializers.ModelSerializer):
	sitios = RutaSitioSerializer(source='rutasitio_set', many=True)
	class Meta:
		model = Ruta