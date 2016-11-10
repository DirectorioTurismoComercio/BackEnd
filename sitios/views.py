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
from sitios.photo_processing import *
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from sitios.inflector.inflector import Inflector
from django.conf import settings
from sitios.inflector.rules.spanish import Spanish
from django.http import HttpResponse
import plataforma
import re
from translator import  translator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from operator import itemgetter
import json




class SitioList(generics.ListAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer

    def get_queryset(self):
        raw_query = "SELECT DISTINCT sitios_sitio.id, sitios_sitio.nombre, sitios_sitio.telefono, sitios_sitio.whatsapp, sitios_sitio.horariolocal, sitios_sitio.web, sitios_sitio.latitud, sitios_sitio.longitud, sitios_sitio.descripcion, sitios_sitio.correolocal, sitios_sitio.ubicacionlocal, sitios_sitio.usuario_id, sitios_sitio.municipio_id FROM authentication_module_customuser INNER JOIN sitios_sitio ON (authentication_module_customuser.id=sitios_sitio.usuario_id) LEFT OUTER JOIN sitios_sitio_tags ON ( sitios_sitio.id = sitios_sitio_tags.sitio_id ) LEFT OUTER JOIN plataforma_tag ON ( sitios_sitio_tags.tag_id = plataforma_tag.id ) LEFT OUTER JOIN (select z.*, d.tipo as tipopadre from (SELECT a.id AS aid, a.tipo, categoria_id, sitio_id, b . * FROM sitios_sitiocategoria a INNER JOIN plataforma_categoria b ON a.categoria_id = b.id) z left join sitios_sitiocategoria d on z.categoria_padre_id=d.categoria_id and z.sitio_id=d.sitio_id) T6 ON ( sitios_sitio.id = T6.sitio_id ) WHERE ((sitios_sitio.nombre REGEXP '[[:<:]]{original_word}[[:>:]]|[[:<:]]{word}[[:>:]]' OR sitios_sitio.descripcion REGEXP '[[:<:]]{original_word}[[:>:]]|[[:<:]]{word}[[:>:]]' OR plataforma_tag.tag REGEXP '[[:<:]]{original_word}[[:>:]]|[[:<:]]{word}[[:>:]]') OR T6.nombre REGEXP '[[:<:]]{original_word}[[:>:]]|[[:<:]]{word}[[:>:]]') {municipio_query} AND authentication_module_customuser.es_cuenta_activa=1 AND authentication_module_customuser.is_active=1 ORDER BY T6.tipo, T6.tipopadre ASC"
        queryset = super(SitioList, self).get_queryset()
        
        word = self.request.QUERY_PARAMS.get('search', None)
        id_municipio = self.request.QUERY_PARAMS.get('id_municipio', None)
        resultados = {}
        if word is not None:
            inflector = Inflector(Spanish)
            original_word =word
            original_word = remove_accents(original_word.encode('utf-8'))
            original_word = create_accents_regular_expression(original_word)

            word = inflector.singularize(word)
              
            word = remove_accents(word.encode('utf-8'))
            word = create_accents_regular_expression(word)
            regular_expression = r'[[:<:]]'+original_word+'[[:>:]]|[[:<:]]'+word+'[[:>:]]'
            
        if id_municipio is not None:
            municipio_query = "AND sitios_sitio.municipio_id = "+id_municipio
        else:
            municipio_query =""
        
        raw_query = raw_query.format(original_word=original_word,word=word,municipio_query=municipio_query)


        resultados = Sitio.objects.raw(raw_query)

        paginator = Paginator((list(resultados)), 5)

        page = self.request.GET.get('page')
        try:
            resultados = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resultados = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resultados = []

        return resultados


class SitioCreate(generics.CreateAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        data = request.data

        traductor = translator.Translator()
        serializer = SitioSerializer(data=data)
        photos = request.FILES.iteritems()
        serializer.is_valid()
        dir = settings.MEDIA_ROOT  

        if serializer.is_valid():
            newObject = serializer.save()
            newObject.description=traductor.getTranslatedWord(newObject.descripcion)
            newObject.businessOpenningHours = traductor.getTranslatedWord(newObject.horariolocal)
            newObject.save()
            serializer.add_photos_with_abbreviations(photos)
            site_photos = Foto.objects.filter(sitio_id=serializer.data["id"])
            reduce_site_photos(dir,site_photos)

            if "categorias" in data:
                categories = request.data.getlist('categorias');
                if isinstance(categories, list):
                    if categories[0]!="[]":
                        serializer.add_categories(categories)
                else:
                    return Response(data={"categorias": "Categorías debe ser un arreglo"},
                                    status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response(data={"categorias": "Este campo es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)


class SitioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer
    permission_classes = (IsAuthenticated, IsSiteOwner)

    def update(self, request, *args, **kwargs):
        dir = settings.MEDIA_ROOT  
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        photos = request.FILES.iteritems()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        self.get_object().fotos.all().delete()
        serializer.add_photos_with_abbreviations(photos)
        site_photos = Foto.objects.filter(sitio_id=serializer.data["id"])
        reduce_site_photos(dir,site_photos)

        if "categorias" in request.data:
            categories = request.data.getlist('categorias');
            if isinstance(categories, list):
                if categories[0]!="[]":
                    SitioCategoria.objects.filter(sitio=self.get_object().id).all().delete()
                    serializer.add_categories(categories)
            else:
                return Response(data={"categorias": "Categorías debe ser un arreglo"},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(data={"categorias": "Este campo es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)


    def perform_update(self, serializer):
        instance = serializer.save()
        traductor = translator.Translator()
        instance.description = traductor.getTranslatedWord(instance.descripcion)
        instance.businessOpenningHours = traductor.getTranslatedWord(instance.horariolocal)
        instance.save()




class SitiosCercanosARuta(viewsets.ViewSet):
    def list_sites(self, request):

        sites = Sitio.objects.filter(usuario__es_cuenta_activa=1, usuario__is_active=1)
        resultados = []


        puntos = request.data['points']

        paso = 1

        for i in range(0, len(puntos) - (paso + 1), paso):
            radio = (hallar_distancia_geodesica(puntos[i], puntos[i + paso]) / 2)*settings.FACTOR_ESCALA_RADIO_DE_BUSQUEDA_RUTA
            for site in sites:
                distancia = hallar_distancia_geodesica(puntos[i], (site.latitud, site.longitud))
                if distancia <= radio:
                    siteSerializer = SitioSerializer(site, context={'request': request})
                    if not site in resultados:
                        resultados.append(site)

        print ("los resultados", len(resultados))
        paginator = Paginator((list(resultados)), 5)
        resultados = []
        page = self.request.GET.get('page')
        try:
            resultados = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resultados = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resultados = []


        sitios=[]

        for resultado in resultados.object_list:
            siteSerializer = SitioSerializer(resultado, context={'request': request})

            sitios.append(siteSerializer.data)


        return Response(sitios)


class SitioMunicipioList(generics.ListAPIView):
    queryset =  Sitio.objects.filter(tipo_sitio='M',usuario__es_cuenta_activa=True).order_by('nombre')
    serializer_class = SitioSerializer

class SitiosDelMunicipio(generics.ListAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer

    def get_queryset(self):
        queryset = super(SitiosDelMunicipio, self).get_queryset()
        municipio_id = self.request.QUERY_PARAMS.get('municipio_id', None)
        
        return queryset.filter(municipio_id=municipio_id).order_by('nombre')





class Sugerencias(viewsets.ViewSet):
    def list_sugerencias(self, request, token=None):

        token = self.request.QUERY_PARAMS.get('token', None)
        municipio_id = self.request.QUERY_PARAMS.get('municipio_id', None)

        n_espacios = token.count(' ');

        if municipio_id is None:
            resultados = Sitio.objects.filter(nombre__icontains=token);
        else:
            resultados = Sitio.objects.filter(nombre__icontains=token,municipio_id=municipio_id);
            

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

                deleteSpecialCharacters = re.compile(
                    "[^\w| |\xc1|\xe1|\xc9|\xe9|\xcd|\xed|\xbf|\xf3|\xda|\xfa|\xdc|\xfc|\xd1|\xf1]")
                palabra = deleteSpecialCharacters.sub('', palabra)
                palabra = palabra.capitalize()

                if palabra not in sugerencias:
                    sugerencias.append(palabra)

        return Response(sugerencias[0:5])




