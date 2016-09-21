# -*- coding: utf-8 -*-
from django.test import TestCase
from authentication_module.serializers import CustomUserSerializer
from plataforma.models import Municipio
from rutas.models import Ruta,RutaSitio
from sitios.models import Sitio
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
import json


class CRUDRutaTest(TestCase):	
# Create your tests here.

	PASSWORD='12345'
	EMAIL='correo@correo.com'

	def setUp(self):

		
		self.usuario =CustomUserSerializer(data={'email': self.EMAIL,'password': self.PASSWORD, 'first_name':'Carlos','last_name':'Torres'})
		self.usuario.is_valid()
		self.usuario = self.usuario.save()
		self.usuario.set_password(self.PASSWORD)
		self.usuario.save()

		self.municipio = Municipio.objects.create(nombre='Cota',latitud=0,longitud=0)
		
		
		self.sitio=Sitio.objects.create(nombre='Cota',latitud=0,longitud=0,municipio=self.municipio,horariolocal="",usuario=self.usuario)
		self.sitio1=Sitio.objects.create(nombre='Panaderia pan blandito',latitud=0,longitud=0,municipio=self.municipio,horariolocal="7-15",usuario=self.usuario)
		self.sitio2=Sitio.objects.create(nombre='Pan Pan bueno',latitud=0,longitud=0,municipio=self.municipio,horariolocal="7-15",usuario=self.usuario)
		self.sitio3=Sitio.objects.create(nombre='Hotel el holgazan',latitud=0,longitud=0,municipio=self.municipio,horariolocal="7-15",usuario=self.usuario)
		self.sitio4=Sitio.objects.create(nombre='Bar café',latitud=0,longitud=0,municipio=self.municipio,horariolocal="7-15",usuario=self.usuario)

		
		token, created = Token.objects.get_or_create(user=self.usuario)
		self.client =  APIClient()
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
	
	def test_create_successfully(self):
		client =  APIClient()
		nombre_ruta = "ruta de la sal"
		sitios = [
			{'sitio_id':self.sitio1.id, 'orden': 1},
			{'sitio_id':self.sitio2.id, 'orden': 2},
			{'sitio_id':self.sitio3.id, 'orden': 3},
			{'sitio_id':self.sitio4.id, 'orden': 4},
			]


		ruta = {
		    "nombre": nombre_ruta, 
  			"descripcion": "xxx xxxx xxxx xxx xxxx xxx", 
    		"sitio": self.sitio.id, 
    		"tiempo": "0",
    		"distancia": "0",
    		"sitios": [
			{"sitio_id":self.sitio1.id, "orden": 1},
			{"sitio_id":self.sitio2.id, "orden": 2},
			{"sitio_id":self.sitio3.id, "orden": 3},
			{"sitio_id":self.sitio4.id, "orden": 4},
			]

		}
		
		


		response = self.client.post('/ruta/crear', content_type='application/json',
                                    data=json.dumps(ruta))
		
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
		ruta = Ruta.objects.filter(nombre=nombre_ruta)
		self.assertTrue(self.sitio1 in ruta[0].sitios.all())
		self.assertTrue(self.sitio2 in ruta[0].sitios.all())
		self.assertTrue(self.sitio3 in ruta[0].sitios.all())
		self.assertTrue(self.sitio4 in ruta[0].sitios.all())
		




