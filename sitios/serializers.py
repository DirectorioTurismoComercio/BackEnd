# coding=utf-8 

from rest_framework import serializers
from sitios.models import Sitio
from sitios.models import Foto 
from sitios.models import Tag 
from sitios.models import SitioCategoria 
from plataforma.models import Municipio
from plataforma.models import Categoria

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
   class Meta:
        model = SitioCategoria

class SitioSerializer(serializers.ModelSerializer):  
	categoriasID = SitioCategoriaSerializer(source='sitiocategoria_set', many=True)  
	fotos=FotoSerializer(many=True, read_only=True)
	municipio=MunicipioSerializer(read_only=True)
	tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False) 
	municipio_id = serializers.IntegerField()

	
	def to_internal_value(self, data):
		print data.get('categorias')
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
		print categories
		for category in categories:
			print 'Z '*30
			print category
			SitioCategoria.objects.create(sitio_id=self.data["id"],categoria_id=category["categoria_id"],tipo=category["tipo"]);
	
	def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan 
		for tag in tags:
			try:
				tag_object = Tag.objects.get(tag=tag)
			except:
				tag_object = Tag.objects.create(tag=tag)   			
	class Meta:
		model = Sitio


            

