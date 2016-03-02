from django.test import TestCase
from authentication_module.serializers import CustomUserSerializer
from rest_framework import status


class AuthenticationTest(TestCase):
	WRONG_PASSWORD='12346'
	PASSWORD='12345'
	EMAIL='correo@correo.com'

	def setUp(self):
		user = CustomUserSerializer(data={'email':self.EMAIL,'password': self.PASSWORD})
		user.is_valid()
		user = user.save()
		user.set_password(self.PASSWORD)
		user.save()

	def test_succesfully_authenticated(self):
		data={'email':self.EMAIL,'password': self.PASSWORD}
		response = self.client.post('/rest-auth/login',data,format='json')        
		self.assertEqual(response.status_code, status.HTTP_200_OK, response)

	def test_failed_authentication(self):
		data={'email':self.EMAIL,'password': self.WRONG_PASSWORD}
		response = self.client.post('/rest-auth/login',data,format='json')        
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response)
		