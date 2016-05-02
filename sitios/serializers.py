from rest_framework import serializers
from sitios.models import Sitio

class SitioSerializer(serializers.ModelSerializer):  
        class Meta:
            model = Sitio
            fields = ('nombre','latitud','longitud','descripcion','fotos')


