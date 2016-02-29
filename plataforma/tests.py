from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from plataforma.models import *
from plataforma.similarity import *



class CreateUserTest(TestCase):
    rol_id=2
    municipio_id=1
    def setUp(self):
        pregunta=Pregunta.objects.create(enunciado='Donde')
        Rol.objects.create(id=self.rol_id,nombre='Comerciante')
        OpcionesDeRespuesta.objects.create(id=self.municipio_id,respuesta='Cota',
            valor=self.municipio_id,orden=self.municipio_id,pregunta=pregunta)

    def test_succesfully_created(self):

        data = {"nombres": "Alejandro", 
        "apellido1": "Latorre", 
        "apellido2": "Latorre", 
        "correo": "alatoxxxxxxxxxxxxxxxxxxxxxxxxxxxxrr16@aol.comxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 
        "nombre_institucion": "Programador .JS", 
        "telefono_institucion": "9999999", 
        "ubicacion_institucion": "Subachoque", 
        "direccion_institucion": "Calle 24", 
        "password": "12345",
        "rol": self.rol_id,  
        "municipio_id":  self.municipio_id
        } 
        response = self.client.post('/usuarios2/',data,format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response)


class SimilarityTest(TestCase):
	def test_empty_questionnaire(self):
		questionnaire=[]
		self.assertEqual(to_python_object(questionnaire),'{}')
	def test_malformed_questionnaire(self):	
		questionnaire=[{1:"pregunta"}]
		self.assertRaises(Exception,to_python_object,questionnaire)
		

    

	

