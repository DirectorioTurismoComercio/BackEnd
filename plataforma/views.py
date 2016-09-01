# coding=utf-8 

from plataforma.models import *
from rest_framework import status
from plataforma.serializers import *
from sitios.serializers import MunicipioSerializer
from sitios.serializers import CategoriaSerializer
from sitios.permissions import IsSiteOwner
from authentication_module.serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token


from plataforma.similarity import *
from plataforma.emails import *
from django.db.models import Q
import json
import logging 

from rest_framework import permissions

class MunicipiosListCreate(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer  

    
    
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer  
    permission_classes = (IsAuthenticated,IsSiteOwner)



class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer 
    def get_queryset(self):
        queryset = super(CategoriaListCreate, self).get_queryset()
        
        nivel = self.request.QUERY_PARAMS.get('nivel', None)
        padre = self.request.QUERY_PARAMS.get('categoria_padre', None)
      
        if nivel is not None:
          if padre is not None:
            return queryset.filter(nivel=nivel,categoria_padre_id=padre)            
          else:
            return queryset.filter(nivel=nivel)    

        return queryset.filter()  

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer 

class TagDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer 







   

        

