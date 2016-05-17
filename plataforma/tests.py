from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from plataforma.models import *

from mock import Mock

# class CreateUserTest(TestCase):
   
#     def test_succesfully_created(self):

#         data = {"nombres": "Alejandro", 
#         "apellidos": "Latorre", 
#         "correo": "alatoxxxxxxxxxxxxxxxxxxxxxxxxxxxxrr16@aol.comxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 
#         "telefonos": "9999999", 
#         "password": "12345",
#         } 
#         response = self.client.post('/usuarios/',data,format='json')
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED, response)


