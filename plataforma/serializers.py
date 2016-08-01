# coding=utf-8 

from django.forms import widgets
from rest_framework import serializers
from plataforma import models
from plataforma.models import Categoria
from plataforma.models import Tag
from django.contrib.auth.models import User




              
# # Serializador del modelo Usuario      
# class UsuarioSerializer(serializers.ModelSerializer):
#    sitios = SitioSerializer(many=True, read_only=True) 
#    class Meta:
#         model = Usuario

# Serializador del modelo Categoría
class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Categoria


# Serializador del modelo Tag
class TagSerializer(serializers.ModelSerializer):
   class Meta:
        model = Tag

 


