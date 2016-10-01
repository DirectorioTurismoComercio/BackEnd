# coding=utf-8 

from rest_framework import serializers
from sitios.models import Sitio
from sitios.models import Foto 
from sitios.models import Tag 
from sitios.models import SitioCategoria 
from plataforma.models import Municipio
from plataforma.models import Categoria
from rutas.serializers import *
from rutas.models import Ruta,RutaSitio

class MunicipioSerializer(serializers.ModelSerializer):
  class Meta:
        model = Municipio

class FotoSerializer(serializers.ModelSerializer):  
		class Meta:
			model = Foto

# Serializador del modelo Categoría
class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Categoria

class SitioCategoriaSerializer(serializers.ModelSerializer):
   categoria = CategoriaSerializer(read_only=True)  
   categoria_id = serializers.IntegerField()
   class Meta:
        model = SitioCategoria

class SitioEnRutaSerializer(serializers.ModelSerializer):  
	categorias = SitioCategoriaSerializer(source='sitiocategoria_set', many=True)
	fotos=FotoSerializer(many=True, read_only=True)
	municipio=MunicipioSerializer(read_only=True)
	tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False) 
	municipio_id = serializers.IntegerField()
	class Meta:
		model = Sitio

class RutaSitioSerializer(serializers.ModelSerializer):
	sitio = SitioEnRutaSerializer(read_only=True) 
	sitio_id = serializers.IntegerField()
	ordering = ('-orden',)
	class Meta:
		model = RutaSitio



class RutaSerializer(serializers.ModelSerializer):
	
	sitios = RutaSitioSerializer(source='rutasitio_set', many=True,read_only=True)

	def add_sites_to_route(self, sites):
		for sitio in sites:
			
			sitio["ruta"] = self.data["id"]

			ruta_sitio = RutaSitioSerializer(data=sitio)
			if ruta_sitio.is_valid():
				ruta_sitio.save()
			else:
				raise serializers.ValidationError(ruta_sitio.errors)


		

	class Meta:
		model = Ruta


class SitioSerializer(serializers.ModelSerializer):  
	categorias = SitioCategoriaSerializer(source='sitiocategoria_set', many=True)
	fotos=FotoSerializer(many=True, read_only=True)
	rutas=RutaSerializer(many=True, read_only=True)
	municipio=MunicipioSerializer(read_only=True)
	tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False) 
	municipio_id = serializers.IntegerField()


	
	def to_internal_value(self, data):
		if data.get("tags") is not None:   # si existen tags
			self.check_for_new_tags(data.getlist('tags')) #entonces revisa cuales tags son nuevos
		return super(SitioSerializer,self).to_internal_value(data)

	def add_photos_with_abbreviations(self, fotos):
			
			for nombre, archivo in fotos:
			
				tipoAbreviatura = 'P'

				if 'PRINCIPAL' in nombre:
					tipoAbreviatura = 'P'
				elif 'FACHADA' in nombre:
					tipoAbreviatura = 'F'
				elif 'INTERIOR' in nombre:
					tipoAbreviatura = 'I'
				elif 'PRODUCTOS' in nombre:
					tipoAbreviatura = 'PR'

				z = Foto.objects.create(
                    URLfoto=archivo,
                    sitio_id=self.data["id"],
                    tipo=tipoAbreviatura
                )	

	def add_categories(self,categories):
		for category_string in categories:
			category = eval(category_string)
			if isinstance(category, dict):
				category["sitio"]=self.data["id"]
				serializer = SitioCategoriaSerializer(data=category)
				if serializer.is_valid(raise_exception=True):
					serializer.save()
			else:
				raise serializers.ValidationError("El campo categorias debería ser un arreglo de objetos cada uno con los campos: categoria_id y tipo")

			
	
	def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan 
		for tag in tags:
			try:
				tag_object = Tag.objects.get(tag=tag)
			except:
				tag_object = Tag.objects.create(tag=tag)   			
	class Meta:
		model = Sitio


            


