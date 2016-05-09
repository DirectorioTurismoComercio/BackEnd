# -*- coding: utf-8 -*-
import os
from rest_framework import status
from django.test import TestCase
from sitios.models import Sitio
from sitios.models import Foto
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

class CrearSitioTest(TestCase):

	def test_create_successfully(self):
		new_site = {
		    "nombre": "Café Bar", 
  			"latitud": 4.13, 
    		"longitud": 74.23, 
    		"descripcion": "Breve descripción", 
		}
		response = self.client.post('/sitio',
                                    new_site)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)


	def test_create_successfully_with_photos(self):
		dir = os.path.abspath(os.path.dirname(__file__)) + "/test_photos/"
		nombreFoto1="piqueteadero.jpg"
		nombreFoto2="piqueteadero2.jpg"
		fp1=open(os.path.join(os.pardir, dir+nombreFoto1),'rb')
		fp2=open(os.path.join(os.pardir, dir+nombreFoto2),'rb')
		new_site = {
		    	"nombre": "Café Bar", 
  				"latitud": 4.13, 
    			"longitud": 74.23, 
    			"descripcion": "Breve descripción",
    			"foto1": fp1,
    			"foto2": fp2
			}
		
		response = self.client.post('/sitio',new_site)
		
		self.assertEqual(len(Foto.objects.all()),2)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

	def test_create_bad_request(self):
		new_site = {
  			"latitud": 4.13, 
    		"longitud": 74.23, 
    		"descripcion": "Breve descripción", 
		}
		response = self.client.post('/sitio',new_site)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)



class BusquedaSitioTest(TestCase):

	def setUp(self):
		self.sitio1=Sitio.objects.create(nombre='Panaderia pan blandito',latitud=0,longitud=0)
		self.sitio2=Sitio.objects.create(nombre='Pan Pan bueno',latitud=0,longitud=0)
		self.sitio3=Sitio.objects.create(nombre='Hotel el holgazan',latitud=0,longitud=0)
		self.sitio4=Sitio.objects.create(nombre='Bar café',latitud=0,longitud=0)
		self.sitio5=Sitio.objects.create(nombre='Cafe Bar',latitud=0,longitud=0)
		self.sitio6=Sitio.objects.create(nombre='En el bar del tango',latitud=0,longitud=0)
		self.sitio7=Sitio.objects.create(nombre='Barranquilla',latitud=0,longitud=0)
		self.sitio8=Sitio.objects.create(nombre='Santa Barbara',latitud=0,longitud=0)
		self.sitio9=Sitio.objects.create(nombre='Baño público',latitud=0,longitud=0)
		
	def test_busqueda(self):
		resultados = self.client.get('/buscar/?search=bar');
		resultados = {resultado['nombre'] for resultado in resultados.data}
		
		self.assertTrue(self.sitio4.nombre.decode('utf8') in resultados)
		self.assertTrue(self.sitio5.nombre in resultados)
		self.assertTrue(self.sitio5.nombre in resultados)
		self.assertTrue(self.sitio6.nombre in resultados)

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
			

	def test_sugerencias(self):
		palabras_esperadas = [u'Panaderia',u'Pan']
		resultados = self.client.get('/sugerencias/?token=pa')
		self.assertItemsEqual(palabras_esperadas,resultados.data)	

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
		
