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

 


