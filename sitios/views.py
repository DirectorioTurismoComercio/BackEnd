from sitios.serializers import SitioSerializer
from sitios.models import Sitio
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response


class SitioListCreate(generics.ListCreateAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerializer 
    
    def get_queryset(self):
        queryset = super(SitioListCreate, self).get_queryset()       
        search = self.request.QUERY_PARAMS.get('search', None)

        if search is not None:
          return queryset.filter(nombre__icontains=search)
          
        return queryset.filter()



class Sugerencias(viewsets.ViewSet):
    def list_sugerencias(self,request,token=None):

      token = self.request.QUERY_PARAMS.get('token', None)

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
