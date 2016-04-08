# coding=utf-8 

from django.forms import widgets
from rest_framework import serializers
from plataforma import models
from plataforma.models import Usuario
from plataforma.models import Categoria
from plataforma.models import Tag
from plataforma.models import Municipio
from django.contrib.auth.models import User



# Serializador de los Municipios para el registro y para las preguntas. Corresponde al nodelo OpcionesDeRespuesta
class MunicipioSerializer(serializers.ModelSerializer):
  class Meta:
        model = Municipio
              
# Serializador del modelo Usuario      
class UsuarioSerializer(serializers.ModelSerializer):
   tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False)
    
   def to_internal_value(self, data):
      if data.get("tags") is not None:   # si existen tags
        self.check_for_new_tags(data.get("tags")) #entonces revisa cuales tags son nuevos
      return super(UsuarioSerializer,self).to_internal_value(data)

   def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan 
      for tag in tags:
        try:
             tag_object = Tag.objects.get(tag=tag)
        except:
             tag_object = Tag.objects.create(tag=tag)   
   class Meta:
        model = Usuario

# Serializador del modelo Categoría
class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Categoria


# Serializador del modelo Tag
class TagSerializer(serializers.ModelSerializer):
   class Meta:
        model = Tag

 


