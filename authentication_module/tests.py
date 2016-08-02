from django.test import TestCase
from authentication_module.serializers import CustomUserSerializer
from rest_framework import status


class AuthenticationTest(TestCase):
	WRONG_PASSWORD='12346'
	PASSWORD='1234567'
	email='email@email.com'

	def setUp(self):
		user = CustomUserSerializer(data={'email': self.email,'password': self.PASSWORD, 'first_name':'Carlos','last_name':'Torres'})
		user.is_valid()
		user = user.save()
		user.set_password(self.PASSWORD)
		user.save()

	def test_succesfully_authenticated(self):
		data={'email':self.email,'password': self.PASSWORD}
		response = self.client.post('/rest-auth/login/',data,format='json')        
		self.assertEqual(response.status_code, status.HTTP_200_OK, response)

	def test_failed_authentication(self):
		data={'email':self.email,'password': self.WRONG_PASSWORD}
		response = self.client.post('/rest-auth/login/',data,format='json')        
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response)


class RegistrationTest(TestCase):
	
	PASSWORD='1234567'
	email='email@email.com'


	def setUp(self):
		user = CustomUserSerializer(data={'email':self.email,'password': self.PASSWORD})
		user.is_valid()
		user = user.save()
		user.set_password(self.PASSWORD)
		user.save()

	

	def test_succesful_registration(self):
		email ="perez.juan@gmail.com"
		password = '1234567'
		data={'email':email,'password1': password,'password2': password, 'first_name':'Juan', 'last_name':'perez'}
		response = self.client.post('/rest-auth/registration/',data,format='json')        
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.status_code)

	def test_existing_email(self):
	
		data = {"nombres": "Alejandro", 
        "apellidos": "Latorre", 
        "email": self.email,
        "password1": self.PASSWORD,
        "password2": self.PASSWORD,
        } 
		response = self.client.post('/rest-auth/registration/',data,format='json')        
        
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response)








		