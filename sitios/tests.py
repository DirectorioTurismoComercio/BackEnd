from django.test import TestCase
from sitios.models import Sitio
from search_suggestions import generate_string_suggestions

class BusquedaSitioTest(TestCase):

	def setUp(self):
		self.sitio1=Sitio.objects.create(nombre='Panaderia pan blandito',latitud=0,longitud=0)
		self.sitio2=Sitio.objects.create(nombre='Pan Pan bueno',latitud=0,longitud=0)
		self.sitio3=Sitio.objects.create(nombre='Hotel el holgazan',latitud=0,longitud=0)
        
        
	def test_busqueda(self):
		resultados = self.client.get('/buscar/?search=Pan');
		resultados = {resultado['nombre'] for resultado in resultados.data}

		self.assertTrue(self.sitio1.nombre in resultados)
		self.assertTrue(self.sitio2.nombre in resultados)
		self.assertFalse(self.sitio3.nombre in resultados)

	def test_sugerencias(self):
		palabras_esperadas = [u'Panaderia',u'Pan']
		resultados = self.client.get('/sugerencias/?token=pa')
		self.assertItemsEqual(palabras_esperadas,resultados.data)	


class SuggestionsTest(TestCase):

	def test_generate_suggestions(self):
		string_array=['Panaderia Don Juan','pan pan','Panpaya','pan de a mil','pan123','uno trapan']
		expected_results=['Panaderia', 'pan pan', 'Panpaya', 'pan de','pan123']
		string='pan'
		results=generate_string_suggestions(string,string_array)
		self.assertItemsEqual(expected_results,results,results)	


