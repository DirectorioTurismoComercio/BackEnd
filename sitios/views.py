from sitios.models import Foto
from sitios.models import Sitio
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.response import Response
from sitios.distancia import *
from sitios.serializers import SitioSerializer
from sitios.serializers import FotoSerializer
from django.db.models import Q
import plataforma

class SitioListCreate(generics.ListCreateAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer 
    

    def get_queryset(self):
        queryset = super(SitioListCreate, self).get_queryset()       
        word = self.request.QUERY_PARAMS.get('search', None)
        id_municipio = self.request.QUERY_PARAMS.get('id_municipio', None)
        resultados={}
        if word is not None:
          if id_municipio is not None:

              resultados= queryset.filter(
              Q(nombre__istartswith=word+' ') |
              Q(nombre__icontains=' '+word+' ') |
              Q(nombre__iendswith=' '+word) |
              Q(nombre=word) ,
              Q(municipio_id=id_municipio)
              ) ;

          else:
              resultados=  queryset.filter(
              Q(nombre__istartswith=word+' ') |
              Q(nombre__icontains=' '+word+' ') |
              Q(nombre__iendswith=' '+word) |
              Q(nombre=word) 
              ) ;

        return resultados

    def create(self,request):
      datos=request.data
      print("datos",datos)
      dictdatos=dict(request.POST.iterlists())
      print("dict",dictdatos)

      serializer = SitioSerializer(data=dictdatos)
      if serializer.is_valid():
        serializer.save()
        for key, foto in request.FILES.iteritems():
          Foto.objects.create(
          URLfoto=foto,
          sitio_id=serializer.data["id"]
          )
      else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

      
      return Response(status=status.HTTP_201_CREATED)

class SitiosCercanosARuta(viewsets.ViewSet):
  def list_sites(self,request):
    sites=Sitio.objects.all()
    
    resultados=[]

    puntos=request.data['points']
    paso=1

    for i in range(0,len(puntos)-(paso+1),paso):
      radio=hallar_distancia_geodesica(puntos[i],puntos[i+paso])/2
      for site in sites:
        distancia=hallar_distancia_geodesica(puntos[i],(site.latitud,site.longitud))
        if distancia<= radio:
          if not site in resultados:
            siteSerializer=SitioSerializer(site)
            resultados.append(siteSerializer.data)

    return Response(resultados)

class Sugerencias(viewsets.ViewSet):
    def list_sugerencias(self,request,token=None):

      token = self.request.QUERY_PARAMS.get('token', None)
      print (token)

      n_espacios = token.count(' ');
      resultados = Sitio.objects.filter(nombre__icontains=token); 
        
      sugerencias=[]
      for resultado in resultados:
           posicion = resultado.nombre.upper().find(token.upper());
           if posicion>0:
            posicion = resultado.nombre.upper().find(token.upper());
           s=resultado.nombre
           if posicion==0 or not(resultado.nombre[posicion-1].isalpha()): 
              pos_espacios=[i for i, letter in enumerate(resultado.nombre[posicion:]) if letter == ' ']
              if pos_espacios:
                 if n_espacios==0:
                   if resultado.nombre[posicion+len(token)]==' ':
                     if len(pos_espacios)>1:
                       palabra = resultado.nombre[posicion:posicion+pos_espacios[1]]                    
                     else:
                       palabra = resultado.nombre[posicion:] 
                       
                   else: 
                     palabra = resultado.nombre[posicion:posicion+pos_espacios[0]]

                 else:
                   if n_espacios+1<len(pos_espacios): 
                     palabra = resultado.nombre[posicion:posicion+pos_espacios[n_espacios+1]]
                   else:
                     palabra = resultado.nombre[posicion:]
              else:
                palabra = resultado.nombre[posicion:]  


              try: 
                sugerencias.index(palabra)
                
              except ValueError:
                sugerencias.append(palabra)
                

      return Response(sugerencias[0:5]) 
          
    def list_sugerencias_tags(self,request,token=None):

      token = self.request.QUERY_PARAMS.get('token', None)

      n_espacios = token.count(' ');
      resultados = Tag.objects.filter(tag__icontains=token); 
      
      
  
      sugerencias=[]
      for resultado in resultados:
           posicion = resultado.tag.upper().find(token.upper());
           if posicion>0:
            posicion = resultado.tag.upper().find(token.upper());
           s=resultado.tag
           if posicion==0 or not(resultado.tag[posicion-1].isalpha()): 
              pos_espacios=[i for i, letter in enumerate(resultado.tag[posicion:]) if letter == ' ']
              if pos_espacios:
                 if n_espacios==0:
                   if resultado.tag[posicion+len(token)]==' ':
                     if len(pos_espacios)>1:
                       palabra = resultado.tag[posicion:posicion+pos_espacios[1]]                    
                     else:
                       palabra = resultado.tag[posicion:] 
                       
                   else: 
                     palabra = resultado.tag[posicion:posicion+pos_espacios[0]]

                 else:
                   if n_espacios+1<len(pos_espacios): 
                     palabra = resultado.tag[posicion:posicion+pos_espacios[n_espacios+1]]
                   else:
                     palabra = resultado.tag[posicion:]
              else:
                palabra = resultado.tag[posicion:]  


              try: 
                sugerencias.index(palabra)
                
              except ValueError:
                sugerencias.append(palabra)
                

      return Response(sugerencias[0:5]) 
