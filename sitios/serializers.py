# coding=utf-8 

from rest_framework import serializers
from sitios.models import Sitio
from sitios.models import Foto 
from sitios.models import Tag 


class FotoSerializer(serializers.ModelSerializer):  
		class Meta:
			model = Foto

class SitioSerializer(serializers.ModelSerializer):  
	fotos=FotoSerializer(many=True, read_only=True)
	tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False)
    
	def to_internal_value(self, data):
		data["nombre"]=(data.get("nombre")[0]).encode('utf-8')
		data["horariolocal"]=(data.get("horariolocal")[0]).encode('utf-8')
		data["descripcion"]=(data.get("descripcion")[0]).encode('utf-8')
		data["correolocal"]=(data.get("correolocal")[0]).encode('utf-8')
		data["ubicacionlocal"]=(data.get("ubicacionlocal")[0]).encode('utf-8')
		data["telefono"]=int(data.get("telefono")[0])
		data["latitud"]=float(data.get("latitud")[0])
		data["longitud"]=float(data.get("longitud")[0])
		data["municipio"]=int(data.get("municipio")[0])

		if data.get("tags") is not None:   # si existen tags
			self.check_for_new_tags(data.get("tags")) #entonces revisa cuales tags son nuevos
		return super(SitioSerializer,self).to_internal_value(data)

	def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan 
		for tag in tags:
			try:
				tag_object = Tag.objects.get(tag=tag)
			except:
				tag_object = Tag.objects.create(tag=tag)   
	class Meta:
		model = Sitio


            

