from rest_framework import serializers
from sitios.models import Sitio
from sitios.models import Foto 

class FotoSerializer(serializers.ModelSerializer):  
		class Meta:
			model = Foto

class SitioSerializer(serializers.ModelSerializer):  
		fotos=FotoSerializer(many=True)
		class Meta:
			model = Sitio
			#fields = ('nombre','latitud','longitud','descripcion')


            

