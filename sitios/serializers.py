# coding=utf-8 

from rest_framework import serializers
from sitios.models import Sitio
from sitios.models import Foto 
from sitios.models import Tag 
from plataforma.serializers import MunicipioSerializer


class FotoSerializer(serializers.ModelSerializer):  
		class Meta:
			model = Foto

class SitioSerializer(serializers.ModelSerializer):  
	fotos=FotoSerializer(many=True, read_only=True)
	municipio=MunicipioSerializer(read_only=True)
	tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False)
	municipio_id = serializers.IntegerField()
	def to_internal_value(self, data):
		if "nombre" in data:
			data["nombre"]=(data.get("nombre")[0])
		if "horariolocal" in data:
			data["horariolocal"]=(data.get("horariolocal")[0])
		if "descripcion" in data: 
			data["descripcion"]=(data.get("descripcion")[0])
		if "correolocal" in data:
			data["correolocal"]=(data.get("correolocal")[0])
		if "ubicacionlocal" in data:
			data["ubicacionlocal"]=(data.get("ubicacionlocal")[0])
		if "telefono" in data:
			data["telefono"]=int(data.get("telefono")[0])
		if "whatsapp" in data:
			data["whatsapp"]=(data.get("whatsapp")[0])
		if "web" in data:
			data["web"]=(data.get("web")[0])
		if "latitud" in data:
			data["latitud"]=float(data.get("latitud")[0])
		if "longitud" in data: 
			data["longitud"]=float(data.get("longitud")[0])
		if "municipio_id" in data: 
			data["municipio_id"]=int(data.get("municipio_id")[0])
		if "usuario" in data: 
			data["usuario"]=int(data.get("usuario")[0])	

		if data.get("tags"):   # si existen tags
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


            

