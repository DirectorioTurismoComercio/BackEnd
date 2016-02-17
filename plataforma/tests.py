from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from plataforma.models import *

from mock import Mock



# class ToPythonObjectTest(TestCase):
# 	def test_empty_questionnaire(self):
# 		questionnaire=[]
# 		self.assertEqual(to_python_object(questionnaire),'{}')
# 	def test_malformed_questionnaire(self):	
# 		questionnaire=[{1:"pregunta"}]
# 		self.assertRaises(Exception,to_python_object,questionnaire)


from plataforma import similarity
similarity.to_python_object = Mock(return_value='{111}')
from plataforma.similarity import cuestionario_afinidad


class CuestionarioAfinidadTest(TestCase):	
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

