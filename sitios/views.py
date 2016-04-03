from sitios.serializers import SitioSerializer
from sitios.models import Sitio
from sitios.search_suggestions import generate_string_suggestions
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
    def list_sugerencias(self,request):

      token = self.request.QUERY_PARAMS.get('token', None)
      resultados = Sitio.objects.filter(nombre__icontains=token);        
      sugerencias=[]          
      string_array = [resultado.nombre for resultado in resultados]  
      sugerencias = generate_string_suggestions(token, string_array)

      return Response(sugerencias[0:5]) 
          
    