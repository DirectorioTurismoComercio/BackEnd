from sitios.serializers import SitioSerializer
from sitios.models import Sitio
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from sitios.distancia import *


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

class SitiosCercanosARuta(viewsets.ViewSet):
  def list_sites(self,request):
    sites=Sitio.objects.all()
    parametroB=0.01
    resultados=[]

    puntos=request.data['points']
    paso=1


    for i in range(0,len(puntos)-(paso+1),paso):
      puntoInicial=puntos[i]
      puntoFinal=puntos[i+1]
     
      
      coordenadaInicial=geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1]))
      coordenadaFinal=geodesica_a_cartesiana((puntoFinal[0],puntoFinal[1]))
      anguloRotado=hallar_angulo_rotacion(coordenadaInicial,coordenadaFinal)


      puntoInicialRotado=hallar_punto_rotado(coordenadaInicial,anguloRotado)
      puntoFinalRotado=hallar_punto_rotado(coordenadaFinal,anguloRotado)

      a=hallar_distancia_sin_rotar(coordenadaInicial,coordenadaFinal)/2


      distancia_Translacion_En_X=hallar_distancia_traslacion_X(puntoInicialRotado[0],a)
      distancia_Translacion_En_Y=puntoInicialRotado[1]

      #print("coordenadaInicial",coordenadaInicial,"coordenadaFinal",coordenadaFinal,"anguloRotado",anguloRotado,"puntoInicialRotado",puntoInicialRotado,"puntoFinalRotado",puntoFinalRotado,"a",a,"distancia_Translacion_En_X",distancia_Translacion_En_X,"distancia_Translacion_En_Y",distancia_Translacion_En_Y)

      if parametroB<a:
        b=parametroB
      else:
        b=a


      for site in sites:
        coordenada=geodesica_a_cartesiana((site.latitud,site.longitud))
        puntoRotado=hallar_punto_rotado(coordenada,anguloRotado)

        puntoRotadoYTrasladadoX=hallar_coordenada_trasladada(puntoRotado[0],distancia_Translacion_En_X)
        puntoRotadoYTrasladadoY=hallar_coordenada_trasladada(puntoRotado[1],distancia_Translacion_En_Y)
        
        if esta_dentro_de_elipse(a,b,puntoRotadoYTrasladadoX,puntoRotadoYTrasladadoY):
          print("punto inicial",puntoInicial,"punto final",puntoFinal)
          print("El lugar fue",site.nombre,"Punto rotado",puntoRotado,"valor de a", a, "valor de b", b, "valor de x", puntoRotadoYTrasladadoX, "y", puntoRotadoYTrasladadoY)
          siteSerializer=SitioSerializer(site)
          resultados.append(siteSerializer.data)



    #b=hallar_distancia_geodesica(puntoInicial,puntoFinal)/2
    
    #a=2

    #print("El valor de A //////", a)

    #results=[]
    #for site in sites:
     # puntoCartesiano=geodesica_a_cartesiana((site.latitud,site.longitud))
      #print("El valor de punto cartesiano //////", puntoCartesiano)
      #if( dentro_de_elipse(a,b,puntoCartesiano[0],puntoCartesiano[1])):
       # results.add(site)
    
    return Response(resultados)
