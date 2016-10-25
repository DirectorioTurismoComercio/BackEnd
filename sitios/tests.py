# -*- coding: utf-8 -*-
import os
import time
from authentication_module.serializers import CustomUserSerializer
from rest_framework import status
from django.test import TestCase, RequestFactory
from sitios.models import Sitio
from sitios.models import Foto
from plataforma.models import Municipio
from plataforma.models import Categoria
from plataforma.models import Tag
from search_suggestions import generate_string_suggestions
from sitios.distancia import hallar_distancia_geodesica
from sitios.distancia import geodesica_a_cartesiana
from sitios.distancia import hallar_angulo_rotacion
from sitios.distancia import hallar_punto_rotado
from sitios.distancia import hallar_distancia_sin_rotar
from sitios.distancia import hallar_a
from sitios.distancia import hallar_distancia_traslacion_X
from sitios.distancia import hallar_coordenada_trasladada
from sitios.distancia import esta_dentro_de_elipse
from django.http import QueryDict
from sitios.views import SitioDetail
from sitios.models import SitioCategoria
from sitios.string_processing import *
from django.test.client import encode_multipart
from decimal import *
from turismo import settings
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class CRUDSitioTest(TestCase):
	PASSWORD='12345'
	EMAIL='correo@correo.com'
	
	def setUp(self):
		self.factory = RequestFactory()
		self.usuario =CustomUserSerializer(data={'email': self.EMAIL,'password': self.PASSWORD, 'first_name':'Carlos','last_name':'Torres'})
		self.usuario.is_valid()
		self.usuario = self.usuario.save()
		self.usuario.set_password(self.PASSWORD)
		self.usuario.save()

		self.municipio = Municipio.objects.create(nombre='Cota',latitud=0,longitud=0)
		self.municipio2 = Municipio.objects.create(nombre='Tengo',latitud=0,longitud=0)
		self.categoria = Categoria.objects.create(nombre="Comida")
		self.categoria2 = Categoria.objects.create(nombre="Hospedaje")
		
		self.sitio1=Sitio.objects.create(nombre='Panaderia pan blandito',latitud=0,longitud=0,municipio=self.municipio,horariolocal="7-15",usuario=self.usuario)

		SitioCategoria.objects.create(sitio=self.sitio1,categoria=self.categoria);

		self.tag1 = Tag.objects.create(tag='baño')
		tag2 = Tag.objects.create(tag='restaurante')
		tag3 = Tag.objects.create(tag='pollo')
		self.sitio1.tags.add(self.tag1)
		self.sitio1.tags.add(tag2)
		token, created = Token.objects.get_or_create(user=self.usuario)
		self.client =  APIClient()
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
	
	def test_create_successfully(self):

		new_site = {
		    "nombre": "Café Bar", 
  			"latitud": 4.13, 
    		"longitud": 74.23, 
    		"descripcion": "Breve descripción",
    		"municipio_id": self.municipio.id,
    		"categorias": [{"categoria_id":self.categoria.id, "tipo":1}, {"categoria_id":self.categoria2.id, "tipo":1}],
    		"usuario": self.usuario.id
		}

		qdict = QueryDict('', mutable=True)
		qdict.update(new_site)
		response = self.client.post('/sitio',
                                    qdict)
		sitio=Sitio.objects.filter(nombre="Café Bar").all()[0]
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
		self.assertTrue(self.categoria in sitio.categorias.all())
		self.assertTrue(self.categoria2 in sitio.categorias.all())
		self.assertTrue(sitio.description=='Brief description' or sitio.description=='Short description')


	def test_not_authenticated_user_cant_create_site(self):
		client =  APIClient()
		new_site = {
		    "nombre": "Café Bar", 
  			"latitud": 4.13, 
    		"longitud": 74.23, 
    		"descripcion": "Breve descripción",
    		"municipio_id": self.municipio.id,
    		"categorias": [{"categoria_id":self.categoria.id, "tipo":1}, {"categoria_id":self.categoria2.id, "tipo":1}],
    		"usuario": self.usuario.id
		}

		qdict = QueryDict('', mutable=True)
		qdict.update(new_site)
		response = client.post('/sitio',
                                    qdict)
		
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.status_code)
		

	def test_create_successfully_with_photos(self):
		dir = settings.MEDIA_ROOT  + "/test_photos/"
		nombreFoto1="test_13221_piqueteadero.jpg"
		nombreFoto2="test_13221_piqueteadero2.jpg"
		fp1=open(os.path.join(os.pardir, dir+nombreFoto1),'rb')
		fp2=open(os.path.join(os.pardir, dir+nombreFoto2),'rb')
		new_site = {
		    	"nombre": "Café Bar", 
  				"latitud": 4.13, 
    			"longitud": 74.23, 
    			"descripcion": "Breve descripción",
    			"municipio_id": self.municipio.id,
    			"categorias": [{"categoria_id":self.categoria.id, "tipo":2}],
    			"PRINCIPAL_foto1": fp1,
    			"FACHADA_foto2": fp2,
    			"usuario": self.usuario.id
			}
		qdict = QueryDict('', mutable=True)
		qdict.update(new_site)
		
		response = self.client.post('/sitio',new_site)
		
		self.assertEqual(len(Foto.objects.all()),2)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

	def test_create_successfully_with_photos_size_reduction(self):
		dir = settings.MEDIA_ROOT  + "/test_photos/"
		sitio_id = self.sitio1.id
		
		nombreFoto1="test_13221_blob_1.png"
		nombreFoto2="test_13221_paisaje.jpg"
		nombreFoto3="test_13221_fortaleza_1.JPG"

		fp1=open(os.path.join(os.pardir, dir+nombreFoto1),'rb')
		fp2=open(os.path.join(os.pardir, dir+nombreFoto2),'rb')
		fp3=open(os.path.join(os.pardir, dir+nombreFoto3),'rb')
		new_site = {
		    	"nombre": "Café Bar", 
  				"latitud": 4.13, 
    			"longitud": 74.23, 
    			"descripcion": "Breve descripción",
    			"municipio_id": self.municipio.id,
    			"categorias": [{"categoria_id":self.categoria.id, "tipo":2}],
    			"PRINCIPAL_foto1": fp1,
    			"FACHADA_foto2": fp2,
    			"FACHADA_foto3": fp3,
    			"usuario": self.usuario.id
			}
		qdict = QueryDict('', mutable=True)
		qdict.update(new_site)
		
		response = self.client.post('/sitio',new_site)
		
		self.assertEqual(len(Foto.objects.all()),3)
		self.assertTrue(Foto.objects.all()[0].URLfoto.size<settings.MAX_TAMANO_IMAGEN_SIN_REDUCCION,Foto.objects.all()[0].URLfoto.name)
		self.assertTrue(Foto.objects.all()[1].URLfoto.size<settings.MAX_TAMANO_IMAGEN_SIN_REDUCCION,Foto.objects.all()[1].URLfoto.name)
		self.assertTrue(Foto.objects.all()[2].URLfoto.size<settings.MAX_TAMANO_IMAGEN_SIN_REDUCCION,Foto.objects.all()[2].URLfoto.name)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

	def test_create_bad_request(self):
		new_site = {
  			"latitud": 4.13, 
    		"longitud": 74.23, 
    		"descripcion": "Breve descripción", 
    		"categorias":[{"categoria_id":self.categoria.id, "tipo":1}]

		}
		qdict = QueryDict('', mutable=True)
		qdict.update(new_site)
		
		response = self.client.post('/sitio',new_site)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

	def test_update_site_texts(self):
		dir = settings.MEDIA_ROOT  + "/test_photos/"
		sitio_id = self.sitio1.id
		nombreFoto1="test_13221_piqueteadero.jpg"
		nombreFoto2="test_13221_piqueteadero2.jpg"
		fp1=open(os.path.join(os.pardir, dir+nombreFoto1),'rb')
		fp2=open(os.path.join(os.pardir, dir+nombreFoto2),'rb')
		nuevo_nombre = "Nuevo bar"
		nueva_latitud = 2.22
		nueva_longitud = 33.33
		nueva_descripcion = "nuevo dato"
		nuevo_telefono = "1234567"
		nueva_web = "www.abc.com"
		nuevo_whatsapp = "3124131221"
		nuevo_correolocal = "abc@jmail.com"
		nueva_ubicacionlocal = "av 1234"
		new_data = {
		    	"nombre": nuevo_nombre, 
  				"latitud": nueva_latitud, 
    			"longitud": nueva_longitud, 
    			"descripcion": nueva_descripcion,
    			"telefono": nuevo_telefono,
    			"web": nueva_web,
    			"whatsapp": nuevo_whatsapp,
    			"correolocal": nuevo_correolocal,
    			"ubicacionlocal": nueva_ubicacionlocal,
    			"municipio_id": self.municipio2.id,
    			"categorias": [{"categoria_id":self.categoria.id, "tipo":1}],
    			"PRINCIPAL_foto1": fp1,
    			"FACHADA_foto2": fp2,
    			"usuario": self.usuario.id
			}
		qdict = QueryDict('', mutable=True)
		qdict.update(new_data)

		content = encode_multipart('BoUnDaRyStRiNg', new_data)
		content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
		response = self.client.put('/sitio/detail/'+str(sitio_id) ,content_type=content_type, data=content)
		sitio = Sitio.objects.get(pk=sitio_id)
		self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
		self.assertEqual(sitio.nombre, nuevo_nombre)
		self.assertTrue(sitio.longitud- Decimal(nueva_longitud) <0.1)
		self.assertTrue(sitio.latitud- Decimal(nueva_latitud) <0.1)
		self.assertEqual(sitio.descripcion, nueva_descripcion)
		self.assertEqual(sitio.telefono, nuevo_telefono)
		self.assertEqual(sitio.web, nueva_web)
		self.assertEqual(sitio.whatsapp, nuevo_whatsapp)
		self.assertEqual(sitio.correolocal, nuevo_correolocal)
		self.assertEqual(sitio.ubicacionlocal, nueva_ubicacionlocal)
		self.assertEqual(sitio.municipio, self.municipio2)
		self.assertTrue(sitio.description == 'new data')

	def test_update_site_categories_tags(self):
		dir = settings.MEDIA_ROOT + "/test_photos/"
		sitio_id = self.sitio1.id
		
		nuevo_nombre = "Nuevo bar"
		nueva_latitud = 2.22
		nueva_longitud = 33.33
		nueva_descripcion = "nueva descripción"
		nuevo_tag = "pollo"
		new_data = {
		    	"nombre": nuevo_nombre, 
  				"latitud": nueva_latitud, 
    			"longitud": nueva_longitud, 
    			"descripcion": nueva_descripcion,
    			"municipio_id": self.municipio.id,
    			"categorias": [{"categoria_id":self.categoria2.id, "tipo":1}],
    			"tags": [nuevo_tag],
    			"usuario": self.usuario.id
			}
		qdict = QueryDict('', mutable=True)
		qdict.update(new_data)

		content = encode_multipart('BoUnDaRyStRiNg', new_data)
		content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'


		response = self.client.put('/sitio/detail/'+str(sitio_id) ,content_type=content_type, data=content)
		sitio = Sitio.objects.get(pk=sitio_id)
		self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
		self.assertTrue(self.categoria2 in sitio.categorias.all())
		self.assertFalse(self.categoria in sitio.categorias.all())
		tag = Tag.objects.filter(tag=nuevo_tag)[0]
		self.assertTrue(tag in sitio.tags.all())
		self.assertFalse(self.tag1 in sitio.tags.all())

	def test_update_site_photos(self):

		dir = settings.MEDIA_ROOT  + "/test_photos/"
		sitio_id = self.sitio1.id
		nombreFoto1="test_13221_piqueteadero"
		nombreFoto2="test_13221_piqueteadero2"
		nombreFoto3="test_13221_piqueteadero4"
		nombreFoto4="test_13221_piqueteadero5"
		ext=".jpg"
		
		photo1 = Foto.objects.create(URLfoto=os.path.join(os.pardir, settings.MEDIA_ROOT+"/"+nombreFoto1+ext), sitio=self.sitio1, tipo='P')
		photo2 = Foto.objects.create(URLfoto=os.path.join(os.pardir, settings.MEDIA_ROOT+"/"+nombreFoto2+ext), sitio=self.sitio1, tipo='P')

		fp3=open(os.path.join(os.pardir, dir+nombreFoto3+ext),'rb')
		fp4=open(os.path.join(os.pardir, dir+nombreFoto4+ext),'rb')


		nuevo_nombre = "Nuevo bar"
		nueva_latitud = 2.22
		nueva_longitud = 33.33
		nueva_descripcion = "nueva descripción"
		nuevo_tag = "pollo"
		new_data = {
		    	"nombre": nuevo_nombre, 
  				"latitud": nueva_latitud, 
    			"longitud": nueva_longitud, 
    			"descripcion": nueva_descripcion,
    			"municipio_id": self.municipio.id,
    			"categorias": [{"categoria_id":self.categoria.id, "tipo":1}],
    			"tags": [nuevo_tag],
    			"PRINCIPAL_foto3": fp3,
    			"FACHADA_foto4": fp4,
    			"usuario": self.usuario.id
			}

		qdict = QueryDict('', mutable=True)
		qdict.update(new_data)

		content = encode_multipart('BoUnDaRyStRiNg', new_data)
		content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
		response = self.client.put('/sitio/detail/'+str(sitio_id) ,content_type=content_type, data=content, follow=True)
		sitio = Sitio.objects.get(pk=sitio_id)
		self.assertEqual(response.status_code, status.HTTP_200_OK, response)
		self.assertFalse(nombreFoto1 in sitio.fotos.all()[0].URLfoto or nombreFoto1 in sitio.fotos.all()[1].URLfoto)
		self.assertFalse(nombreFoto2 in sitio.fotos.all()[1].URLfoto or nombreFoto2 in sitio.fotos.all()[0].URLfoto)
		
		self.assertTrue(nombreFoto3 in str(sitio.fotos.all()[0].URLfoto) or nombreFoto3 in str(sitio.fotos.all()[1].URLfoto))
		self.assertTrue(nombreFoto4 in str(sitio.fotos.all()[0].URLfoto) or nombreFoto4 in str(sitio.fotos.all()[1].URLfoto))

	def test_delete_site(self):
		dir = settings.MEDIA_ROOT  + "/test_photos/"
		sitio_id = self.sitio1.id
		nombreFoto1="piqueteadero"
		nombreFoto2="piqueteadero2"

		ext=".jpg"
		
		photo1 = Foto.objects.create(URLfoto=os.path.join(os.pardir, dir+nombreFoto1+ext), sitio=self.sitio1, tipo='P')
		photo2 = Foto.objects.create(URLfoto=os.path.join(os.pardir, dir+nombreFoto2+ext), sitio=self.sitio1, tipo='P')
		response = self.client.delete('/sitio/detail/'+str(sitio_id))
		
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)
		self.assertTrue(len(Sitio.objects.filter(pk=sitio_id))==0)	
		self.assertTrue(len(Foto.objects.filter(URLfoto__contains=nombreFoto1))==0) 
		self.assertTrue(len(Foto.objects.filter(URLfoto__contains=nombreFoto2))==0)

	def test_only_owner_can_update(self):
		email2 ='correo2@jmail.com'
		password2 = '1234567'
		user2 = CustomUserSerializer(data={'email': email2,'password': password2, 'first_name':'Carlos','last_name':'Torres'})
		user2.is_valid()
		user2 = user2.save()
		user2.set_password(password2)
		user2.save()
		token2, created = Token.objects.get_or_create(user=user2)
		client2 =  APIClient()
		client2.credentials(HTTP_AUTHORIZATION='Token ' + token2.key)

		sitio_id = self.sitio1.id
		
		nuevo_nombre = "Nuevo bar"
		nueva_latitud = 2.22
		nueva_longitud = 33.33
		nueva_descripcion = "nueva descripción"
		nuevo_tag = "pollo"
		new_data = {
		    	"nombre": nuevo_nombre, 
  				"latitud": nueva_latitud, 
    			"longitud": nueva_longitud, 
    			"descripcion": nueva_descripcion,
    			"municipio_id": self.municipio.id,
    			"categorias": [{"categoria_id":self.categoria.id, "tipo":1}],
    			"tags": [nuevo_tag],
    			"usuario": self.usuario.id
			}
		qdict = QueryDict('', mutable=True)
		qdict.update(new_data)

		content = encode_multipart('BoUnDaRyStRiNg', new_data)
		content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
		response = client2.put('/sitio/detail/'+str(sitio_id) ,content_type=content_type, data=content)
		sitio = Sitio.objects.get(pk=sitio_id)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.status_code)

		
	def tearDown(self):
		dir = settings.MEDIA_ROOT+"/Fotos"
		files = os.listdir(dir)
		for file in files:
			if file.startswith("test_13221"):
				os.remove(os.path.join(dir,file))


		
	
class BusquedaSitioTest(TestCase):
	PASSWORD='12345'
	EMAIL='correo@correo.com'
	

	def setUp(self):
		municipio = Municipio.objects.create(nombre='Cota',latitud=0,longitud=0)
		municipio2 = Municipio.objects.create(nombre='Cajicá',latitud=0,longitud=0)
		self.municipio=municipio
		self.municipio2=municipio2
		usuario = CustomUserSerializer(data={'email': self.EMAIL,'password': self.PASSWORD})
		usuario.is_valid()
		usuario = usuario.save()
		usuario.set_password(self.PASSWORD)
		usuario.save()

		categoria1 = Categoria.objects.create(nombre='sanduches')
		categoria2 = Categoria.objects.create(nombre='cuba')
		tag1 = Tag.objects.create(tag='baño')
		tag2 = Tag.objects.create(tag='restaurante')
		tag3 = Tag.objects.create(tag='hamburguesa')
		self.sitio1=Sitio.objects.create(nombre='Panaderia pan blandito',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio2=Sitio.objects.create(nombre='Pan Pan bueno',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio3=Sitio.objects.create(nombre='Hotel el holgazan',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio4=Sitio.objects.create(nombre='Bar café',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio5=Sitio.objects.create(nombre='Cafe Bar',latitud=0,longitud=0, descripcion='con baño',municipio=municipio2,horariolocal="7-15",usuario=usuario)
		
		SitioCategoria.objects.create(sitio=self.sitio5,categoria=categoria1);
		SitioCategoria.objects.create(sitio=self.sitio5,categoria=categoria2);
		
		self.sitio6=Sitio.objects.create(nombre='En el bar del tango',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio6.tags.add(tag1)
		self.sitio6.tags.add(tag2)
		self.sitio6.tags.add(tag3)
	
		self.sitio7=Sitio.objects.create(nombre='Barranquilla',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio8=Sitio.objects.create(nombre='Santa Barbara',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio8.tags.add(tag2)
		self.sitio9=Sitio.objects.create(nombre='Baño público',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
		self.sitio10=Sitio.objects.create(nombre='Los mejores panes',latitud=0,longitud=0,municipio=municipio,horariolocal="7-15",usuario=usuario)
	
	def test_busqueda(self):
		resultados = self.client.get('/buscar/?search=bar');
		resultados = [resultado['nombre'] for resultado in resultados.data]
		
		self.assertTrue(self.sitio4.nombre.decode('utf8') in resultados)
		self.assertTrue(self.sitio5.nombre in resultados)
		self.assertTrue(self.sitio5.nombre in resultados)
		self.assertTrue(self.sitio6.nombre in resultados)
		self.assertTrue(self.sitio6.nombre in resultados)
		self.assertTrue((resultados).count(self.sitio6.nombre)==1,(resultados).count(self.sitio6.nombre))

		self.assertFalse(self.sitio7.nombre in resultados)
		self.assertFalse(self.sitio8.nombre in resultados)

	def test_busqueda_con_acentos(self):	

		resultados = self.client.get('/buscar/?search=café');
		resultados = {resultado['nombre'] for resultado in resultados.data}
		self.assertTrue(self.sitio4.nombre.decode('utf8') in resultados)
		self.assertTrue(self.sitio5.nombre in resultados)
	
	def test_busqueda_con_ene(self): 
		resultados = self.client.get('/buscar/?search=baño');
		resultados = {resultado['nombre'] for resultado in resultados.data}
		
		self.assertTrue(self.sitio9.nombre.decode('utf8') in resultados)

	def test_coincidencia_exacta(self):
		resultados = self.client.get('/buscar/?search=cafe bar');
		resultados = {resultado['nombre'] for resultado in resultados.data}
		self.assertTrue(self.sitio5.nombre in resultados)


			
	def test_busqueda_por_descripcion(self):
		resultados = self.client.get('/buscar/?search=baño');
		resultados = [resultado['nombre'] for resultado in resultados.data]
		self.assertTrue(self.sitio5.nombre in resultados)
		self.assertTrue((resultados).count(self.sitio5.nombre)==1,(resultados).count(self.sitio5.nombre))

	def test_busqueda_por_tags(self):
		resultados = self.client.get('/buscar/?search=baño');
		resultados = [resultado['nombre'] for resultado in resultados.data]
		
		self.assertTrue(self.sitio6.nombre in resultados)
		self.assertFalse(self.sitio8.nombre in resultados)

	def test_busqueda_por_categoria(self):
		resultados = self.client.get('/buscar/?search=cuba');
		resultados = [resultado['nombre'] for resultado in resultados.data]
		self.assertTrue(self.sitio5.nombre in resultados)

	def test_busqueda_categoria_orden(self):
		categoria3 = Categoria.objects.create(nombre='Deportes')
		categoria4 = Categoria.objects.create(nombre='Comida')
		SitioCategoria.objects.create(sitio=self.sitio6,categoria=categoria3, tipo=1);
		SitioCategoria.objects.create(sitio=self.sitio6,categoria=categoria4, tipo=2);
		SitioCategoria.objects.create(sitio=self.sitio7,categoria=categoria3, tipo=1);
		SitioCategoria.objects.create(sitio=self.sitio7,categoria=categoria4, tipo=2);
		SitioCategoria.objects.create(sitio=self.sitio8,categoria=categoria4, tipo=1);
		resultados = self.client.get('/buscar/?search=comida');
		resultados = resultados.data
		self.assertEquals(resultados[0]['nombre'],self.sitio8.nombre)
		self.assertEquals(resultados[1]['nombre'],self.sitio6.nombre)
		self.assertEquals(resultados[2]['nombre'],self.sitio7.nombre)

	def test_busqueda_subcategoria_orden(self):
		categoria3 = Categoria.objects.create(nombre='Deportes')
		categoria4 = Categoria.objects.create(nombre='Comida')
		subcategoria1 = Categoria.objects.create(nombre='Ciclas',categoria_padre=categoria3, nivel=2)
		subcategoria2 = Categoria.objects.create(nombre='Balones',categoria_padre=categoria3, nivel=2)
		subcategoria3 = Categoria.objects.create(nombre='Hamburguesas',categoria_padre=categoria4, nivel=2)
		subcategoria4 = Categoria.objects.create(nombre='Lechona',categoria_padre=categoria4, nivel=2)
		SitioCategoria.objects.create(sitio=self.sitio6,categoria=categoria3, tipo=1);
		SitioCategoria.objects.create(sitio=self.sitio6,categoria=categoria4, tipo=2);
		SitioCategoria.objects.create(sitio=self.sitio7,categoria=categoria3, tipo=1);
		SitioCategoria.objects.create(sitio=self.sitio7,categoria=categoria4, tipo=2);
		SitioCategoria.objects.create(sitio=self.sitio8,categoria=categoria4, tipo=1);
		
		SitioCategoria.objects.create(sitio=self.sitio6,categoria=subcategoria3);
		SitioCategoria.objects.create(sitio=self.sitio7,categoria=subcategoria3);
		SitioCategoria.objects.create(sitio=self.sitio8,categoria=subcategoria3);

		SitioCategoria.objects.create(sitio=self.sitio6,categoria=subcategoria1);
		SitioCategoria.objects.create(sitio=self.sitio7,categoria=subcategoria1);
		SitioCategoria.objects.create(sitio=self.sitio8,categoria=subcategoria1);

		SitioCategoria.objects.create(sitio=self.sitio6,categoria=subcategoria4);
		SitioCategoria.objects.create(sitio=self.sitio7,categoria=subcategoria4);
		SitioCategoria.objects.create(sitio=self.sitio8,categoria=subcategoria4);

		resultados = self.client.get('/buscar/?search=Lechona');
		resultados = resultados.data

		self.assertEquals(resultados[0]['nombre'],self.sitio8.nombre)
		self.assertEquals(resultados[1]['nombre'],self.sitio6.nombre)
		self.assertEquals(resultados[2]['nombre'],self.sitio7.nombre)



	def test_busqueda_en_municipio(self):
		resultados = self.client.get('/buscar/?search=cafe&id_municipio='+str(self.municipio.id));
		resultados = [resultado['nombre'] for resultado in resultados.data]

		self.assertTrue(self.sitio4.nombre.decode('utf8') in resultados)
		self.assertFalse(self.sitio5.nombre in resultados)

	def test_sugerencias(self):
		palabras_esperadas = [u'Panaderia',u'Pan',u'Panes']
		resultados = self.client.get('/sugerencias/?token=pa')
		self.assertItemsEqual(palabras_esperadas,resultados.data)


class StringProcessingTest(TestCase):
	def test_remove_accents(self):
		self.assertEquals(remove_accents('café'),'cafe')	
		self.assertEquals(remove_accents('cafÉ'),'cafe')
		self.assertEquals(remove_accents('Alcalá'),'alcala')
		self.assertEquals(remove_accents('cáíóúké'),'caiouke')	
		self.assertEquals(remove_accents('cÁÍÓÚkÉ'),'caiouke')	

	def test_create_accents_regular_expression(self):
		self.assertEquals(create_accents_regular_expression('cafe'),'c[aáàäâ]f[eèêéë]')
		


class BusquedaSitiosEnRutaTest(TestCase):

	def setUp(self):
		self.sitio1=Sitio.objects.create(nombre='Panaderia pan blandito',latitud=0,longitud=0)
		self.sitio2=Sitio.objects.create(nombre='Pan Pan bueno',latitud=0,longitud=0)
		self.sitio3=Sitio.objects.create(nombre='Hotel el holgazan',latitud=0,longitud=0)



class HallarDistanciGeodesicaTest(TestCase):

	def test_hallar_distancia(self):
		pointA=(4.5980556, -74.0758333);
		pointB=(4.85, -74.05);
		self.assertEqual(28.168764965411782,hallar_distancia_geodesica(pointA,pointB))

class GeodesicaACartesianaTest(TestCase):

	def test_geodesica_a_cartesiana(self):
		puntoInicial=(4.581442, -74.110850)
		self.assertEqual((-6129.311173562891,509.0338273333693),geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1])))

class HallarAnguloRotacionTest(TestCase):

	def test_hallar_angulo_rotacion(self):
		puntoInicial=(4.582757, -74.103361)
		puntoFinal=(4.586596, -74.098426)
		coordenadaInicial=geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1]))
		coordenadaFinal=geodesica_a_cartesiana((puntoFinal[0],puntoFinal[1]))

		self.assertAlmostEqual(1.9103930795299962,hallar_angulo_rotacion(coordenadaInicial,coordenadaFinal),10)

class HallarPuntoRotadoTest(TestCase):

	def test_hallar_punto_rotado(self):
		puntoInicial=(4.582757, -74.103361)
		puntoFinal=(4.586596, -74.098426)

		coordenadaInicial=geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1]))
		coordenadaFinal=geodesica_a_cartesiana((puntoFinal[0],puntoFinal[1]))

		anguloRotado=hallar_angulo_rotacion(coordenadaInicial,coordenadaFinal)
		puntoEsperado = 1561.5399741072129,-5948.656663685767
		puntoResultado = hallar_punto_rotado(coordenadaInicial,anguloRotado)
		self.assertAlmostEqual(puntoEsperado[0],puntoResultado[0],10)
		self.assertAlmostEqual(puntoEsperado[1],puntoResultado[1],10)


class HallarDistanciaSinRotarTest(TestCase):

	def test_hallar_distancia_sin_rotar(self):
		puntoInicial=(4.582757, -74.103361)
		puntoFinal=(4.586596, -74.098426)

		coordenadaInicial=geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1]))
		coordenadaFinal=geodesica_a_cartesiana((puntoFinal[0],puntoFinal[1]))

		self.assertEqual(0.45141191390249447,hallar_distancia_sin_rotar(coordenadaInicial,coordenadaFinal))

class HallarATestCase:

	def test_hallar_a(self):
		puntoInicial=(4.582757, -74.103361)
		puntoFinal=(4.586596, -74.098426)

		coordenadaInicial=geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1]))
		coordenadaFinal=geodesica_a_cartesiana((puntoFinal[0],puntoFinal[1]))

		distanciaSinRotar=hallar_distancia_sin_rotar(coordenadaInicial,coordenadaFinal)
		self.assertEqual(0.225705957,hallar_a(distanciaSinRotar))

class HallarDistanciaTraslacionX:

	def test_hallar_distancia_traslacion_X(self):
		puntoInicial=(4.582757, -74.103361)
		puntoFinal=(4.586596, -74.098426)

		coordenadaInicial=geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1]))
		coordenadaFinal=geodesica_a_cartesiana((puntoFinal[0],puntoFinal[1]))
		distanciaSinRotar=hallar_distancia_sin_rotar(coordenadaInicial,coordenadaFinal)	

		anguloRotado=hallar_angulo_rotacion(coordenadaInicial,coordenadaFinal)
		puntoRotado=hallar_punto_rotado(coordenadaInicial,anguloRotado)
		puntoRotadoX=puntoRotado[0]
		a=hallar_a(distanciaSinRotar)

		self.assertEqual(1561.3142682266,hallar_distancia_traslacion_X(puntoRotadoX,a))

class HallarCoordenadaTrasladada:

	def test_hallar_coordenada_trasladada(self):
		puntoInicial=(4.582757, -74.103361)
		puntoFinal=(4.586596, -74.098426)

		coordenadaInicial=geodesica_a_cartesiana((puntoInicial[0],puntoInicial[1]))
		coordenadaFinal=geodesica_a_cartesiana((puntoFinal[0],puntoFinal[1]))
			
		anguloRotado=hallar_angulo_rotacion(coordenadaInicial,coordenadaFinal)
		puntoRotado=hallar_punto_rotado(coordenadaInicial,anguloRotado)
		puntoRotadoX=puntoRotado[0]
		a=hallar_a(distanciaSinRotar)
		distanciaTrasladadaX=hallar_distancia_traslacion_X(puntoRotadoX,a)

		self.assertEqual(-0.225705957,hallar_coordenada_trasladada(puntoRotadoX,distanciaTrasladadaX))

class EstaDentroDeElipse:

	def test_esta_dentro_de_elipse(self):
	
		self.assertFalse(esta_dentro_de_elipse(0.4391566855,-0.1665089885,0.225705957,0.1))
		self.assertTrue(esta_dentro_de_elipse(0.1544141681,-0.0082229263,0.225705957,0.1))


# class SuggestionsTest(TestCase):

# 	def test_generate_suggestions(self):
# 		string_array=['Panaderia Don Juan','pan pan','Panpaya','pan de a mil','pan123','uno trapan','Buen pan fresco']
# 		expected_results=['Panaderia', 'pan pan', 'Panpaya', 'pan de','pan123','pan fresco']
# 		string='pan'
# 		results=generate_string_suggestions(string,string_array)
# 		self.assertItemsEqual(expected_results,results,results)	

# 		string='Panaderia Don J'
# 		expected_results=['Panaderia Don Juan']
# 		results=generate_string_suggestions(string,string_array)
# 		self.assertItemsEqual(expected_results,results,results)

# 		string='pan de'
# 		expected_results=['pan de a']
# 		results=generate_string_suggestions(string,string_array)
# 		self.assertItemsEqual(expected_results,results,results)	
		
