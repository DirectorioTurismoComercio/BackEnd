from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from plataforma.models import *
from plataforma.similarity import *



class SimilarityTest(TestCase):
	def test_empty_questionnaire(self):
		questionnaire=[]
		self.assertEqual(to_python_object(questionnaire),'{}')
	def test_malformed_questionnaire(self):	
		questionnaire=[{1:"pregunta"}]
		self.assertRaises(Exception,to_python_object,questionnaire)
		

