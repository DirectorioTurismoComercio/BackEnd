from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from plataforma.models import *
from plataforma.similarity import *
from rest_framework.test import APITestCase




class SimilarityTest(TestCase):
	def test_empty_questionnaire(self):
		questionnaire=[]
		self.assertEqual(to_python_object(questionnaire),'{}')
	def test_malformed_questionnaire(self):	
		questionnaire=[{1:"pregunta"}]
		self.assertRaises(Exception,to_python_object,questionnaire)
		
class CreateUserTest(APITestCase):
    
    def setUp(self):
    	Rol.objects.create(id=2,nombre='Comerciante')

	def test_succesful_created(TestCase):
		url = '/usuarios/'
		data = {"nombres": "Alejandro", 
        "apellido1": "Latorre", 
        "apellido2": "Latorre", 
        "numero_documento": null, 
        "correo": "alatorreaxcasdasaasdasdasdasdasdasdasdasdasdasd16@aol.com", 
        "nombre_institucion": "Programador .JS", 
        "telefono_institucion": "9999999", 
        "ubicacion_institucion": "Subachoque", 
        "direccion_institucion": "Calle 24", 
        "correo_institucion": null, 
        "municipio_id": 96, 
        "rol": 2
        } 
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


