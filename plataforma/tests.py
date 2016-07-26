from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from plataforma.models import *
from authentication_module.serializers import CustomUserSerializer



class CreateUserTest(TestCase):
	PASSWORD='12345'
	EMAIL='correo@correo.com'
	
	def setUp(self):
		user = CustomUserSerializer(data={'email': self.EMAIL,'password': self.PASSWORD})
		user.is_valid()
		user = user.save()
		user.set_password(self.PASSWORD)
		user.save()
   
	def test_succesfully_created(self):

		data = {"nombres": "Alejandro", 
        "apellidos": "Latorre", 
        "correo": "alatoxxxxxxxxxxxxxxxxxxxxxxxxxxxxrr16@aol.comxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",        
        "password": "12345",
        } 
		response = self.client.post('/usuarios/',data,format='json')
        
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response)


	def test_existing_email(self):

		
		data = {"nombres": "Alejandro", 
        "apellidos": "Latorre", 
        "correo": self.EMAIL,
        "password": self.PASSWORD,
        } 
		response = self.client.post('/usuarios/',data,format='json')
        
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response)


