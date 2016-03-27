from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from plataforma.models import *

from mock import Mock


from plataforma import similarity
similarity.to_python_object = Mock(return_value='{111}')
from plataforma.similarity import cuestionario_afinidad


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
		questionnaires=[]
		problemas_soluciones=[]
		pagina=1
		num_registros=10
		expected_answer = {'problemas_soluciones':[], 'total':0}
		self.assertEqual(cuestionario_afinidad(questionnaires,problemas_soluciones,pagina,num_registros),expected_answer)
	def test_malformed_questionnaire(self):	
		questionnaires=[{1:"pregunta"}]
		problemas_soluciones=[]
		pagina=1
		num_registros=10
		expected_answer = {'problemas_soluciones':[], 'total':0}
		self.assertEqual(cuestionario_afinidad(questionnaires,problemas_soluciones,pagina,num_registros),expected_answer)

    

	

