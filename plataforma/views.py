# coding=utf-8 

from plataforma.models import *
from rest_framework import status
from plataforma.serializers import *
from sitios.serializers import MunicipioSerializer
from sitios.serializers import CategoriaSerializer
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

    
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
  
    def create(self, request):
      if 'password' not in request.data:
        password=''
      else: 
        password=request.data['password']    
      if 'correo' not in request.data:
        correo=''
      else:
        correo=request.data['correo']   
      if password=='' or correo=='':
         return Response({'error':'los campos correo y password requeridos'},
                              status=status.HTTP_400_BAD_REQUEST)


      if len(CustomUser.objects.filter(email=correo).all())>0:
        return Response({'error':'E101'},
                              status=status.HTTP_400_BAD_REQUEST)
             
        
      user = CustomUserSerializer(data={'email':correo,'password': password})
      usuario = UsuarioSerializer(data=request.data)
      if user.is_valid():
        if usuario.is_valid(): 
         correo =correo
         nombre = request.data['nombres']+' '+request.data['apellidos']
         user=user.save()
         user.set_password(password);
         user.save()
         token, created = Token.objects.get_or_create(user=user)
         usuario=usuario.save()
         usuario.user = user
         usuario.save()         
         enviar_correo(correo, {"usuario":nombre.upper()})
        else:
         return Response(usuario.errors,
                              status=status.HTTP_400_BAD_REQUEST)  
      else:
        return Response(user.errors,
                              status=status.HTTP_400_BAD_REQUEST)

      return Response({'key': token.key}, status=status.HTTP_201_CREATED)

    
    
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Usuario.objects.get(user_id=self.request.user.id)
   

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
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







   

        

