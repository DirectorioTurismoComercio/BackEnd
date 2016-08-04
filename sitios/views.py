# -*- coding: utf-8 -*-
from sitios.models import Foto
from sitios.models import Sitio
from sitios.models import SitioCategoria
from sitios.permissions import IsSiteOwner
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.response import Response
from sitios.distancia import *
from sitios.serializers import SitioSerializer
from sitios.serializers import SitioCategoriaSerializer
from sitios.serializers import FotoSerializer
from sitios.string_processing import *
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from inflector import *
import plataforma
import re


class SitioList(generics.ListAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer

    def get_queryset(self):
        queryset = super(SitioList, self).get_queryset()
        word = self.request.QUERY_PARAMS.get('search', None)
        id_municipio = self.request.QUERY_PARAMS.get('id_municipio', None)
        resultados = {}
        if word is not None:

            word = remove_accents(word.encode('utf-8'))
            word = create_accents_regular_expression(word)
            regular_expression = r'[[:<:]]'+word+'[[:>:]]'
            
            if id_municipio is not None:

                resultados = queryset.distinct().filter(
                    Q(nombre__iregex=regular_expression) |
                    Q(descripcion__iregex=regular_expression) |
                    Q(tags__tag__iregex=regular_expression) |
                    Q(categorias__nombre__iregex=regular_expression),
                    Q(municipio_id=id_municipio))

            else:
                resultados = queryset.distinct().filter(
                    Q(nombre__iregex=regular_expression)  |
                    Q(descripcion__iregex=regular_expression) |
                    Q(tags__tag__iregex=regular_expression) |
                    Q(categorias__nombre__iregex=regular_expression)
                    )
                

        return resultados

class SitioCreate(generics.CreateAPIView):

    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):     
        data = request.data
        serializer = SitioSerializer(data=data)
        photos = request.FILES.iteritems()
        serializer.is_valid()
           
        if serializer.is_valid():
            serializer.save()
            serializer.add_photos_with_abbreviations(photos)
            if "categorias" in data:
                categories = request.data.getlist('categorias'); 
                if isinstance(categories,list): 
                        
                    serializer.add_categories(categories) 
                else:
                    return Response(data={"categorias":"Categorías debe ser un arreglo"}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response(data={"categorias":"Este campo es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)



class SitioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer
    permission_classes = (IsAuthenticated,IsSiteOwner)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        photos = request.FILES.iteritems()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self.get_object().fotos.all().delete()
        serializer.add_photos_with_abbreviations(photos)

        if "categorias" in request.data:
            categories = request.data.getlist('categorias'); 
            if isinstance(categories,list): 
                    SitioCategoria.objects.filter(sitio=self.get_object().id).all().delete()
                    serializer.add_categories(categories) 
            else:
                    return Response(data={"categorias":"Categorías debe ser un arreglo"}, status=status.HTTP_400_BAD_REQUEST)

        else:
                return Response(data={"categorias":"Este campo es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

        

class SitiosCercanosARuta(viewsets.ViewSet):
    def list_sites(self, request):

        sites = Sitio.objects.all()

        resultados = []

        puntos = request.data['points']

        paso = 1

        for i in range(0, len(puntos) - (paso + 1), paso):
            radio = hallar_distancia_geodesica(puntos[i], puntos[i + paso]) / 2
            for site in sites:
                distancia = hallar_distancia_geodesica(puntos[i], (site.latitud, site.longitud))
                if distancia <= radio:
                    if not site in resultados:
                        siteSerializer = SitioSerializer(site, context={'request': request})
                        if not siteSerializer.data in resultados:
                            resultados.append(siteSerializer.data)

        return Response(resultados)


class Sugerencias(viewsets.ViewSet):
    def list_sugerencias(self, request, token=None):

        token = self.request.QUERY_PARAMS.get('token', None)

        n_espacios = token.count(' ');
        resultados = Sitio.objects.filter(nombre__icontains=token);

        sugerencias = []
        for resultado in resultados:
            posicion = resultado.nombre.upper().find(token.upper());
            if posicion > 0:
                posicion = resultado.nombre.upper().find(token.upper());
            s = resultado.nombre
            if posicion == 0 or not (resultado.nombre[posicion - 1].isalpha()):
                pos_espacios = [i for i, letter in enumerate(resultado.nombre[posicion:]) if letter == ' ']
                if pos_espacios:
                    if n_espacios == 0:
                        if resultado.nombre[posicion + len(token)] == ' ':
                            if len(pos_espacios) > 1:
                                palabra = resultado.nombre[posicion:posicion + pos_espacios[1]]
                            else:
                                palabra = resultado.nombre[posicion:]

                        else:
                            palabra = resultado.nombre[posicion:posicion + pos_espacios[0]]

                    else:
                        if n_espacios + 1 < len(pos_espacios):
                            palabra = resultado.nombre[posicion:posicion + pos_espacios[n_espacios + 1]]
                        else:
                            palabra = resultado.nombre[posicion:]
                else:
                    palabra = resultado.nombre[posicion:]

                deleteSpecialCharacters=re.compile("[^\w| |\xc1|\xe1|\xc9|\xe9|\xcd|\xed|\xbf|\xf3|\xda|\xfa|\xdc|\xfc|\xd1|\xf1]")
                palabra=deleteSpecialCharacters.sub('', palabra)

                if palabra not in sugerencias:
                    sugerencias.append(palabra)

                   

        return Response(sugerencias[0:5])

    