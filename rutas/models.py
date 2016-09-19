from django.db import models
from sitios.models import Sitio
from plataforma.models import Municipio

class Ruta(models.Model):
	sitio = models.ForeignKey(Sitio,blank=False,related_name='rutas')
	nombre = models.CharField(max_length=200, null=False)
	descripcion = models.TextField(null=True)
	sitios = models.ManyToManyField(Sitio, through='RutaSitio')
	tiempo = models.CharField(max_length=200)
	distancia = models.CharField(max_length=200)

class RutaSitio(models.Model):
	sitio = models.ForeignKey(Sitio,blank=False)
	ruta = models.ForeignKey(Ruta,blank=False)
	orden = models.IntegerField()

	class Meta:
		ordering = ('orden',)
