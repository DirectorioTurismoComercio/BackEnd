from django.test import TestCase
from sitios.models import Sitio

class BusquedaSitioTest(TestCase):

	def setUp(self):
		self.sitio1=Sitio.objects.create(nombre='Panaderia pan blandito',latitud=0,longitud=0)
		self.sitio2=Sitio.objects.create(nombre='Panaderia pan pan',latitud=0,longitud=0)
		self.sitio3=Sitio.objects.create(nombre='Hotel el holgazan',latitud=0,longitud=0)
        
        
	def test_busqueda(self):
		resultados = self.client.get('/buscar/?search=panaderia');
		resultados = {resultado['nombre'] for resultado in resultados.data}

		self.assertTrue(self.sitio1.nombre in resultados)
		self.assertTrue(self.sitio2.nombre in resultados)
		self.assertFalse(self.sitio3.nombre in resultados)
