from django.db import models

# Create your models here.

from django.db import models
from plataforma.models import Categoria
from plataforma.models import Municipio

class Sitio(models.Model):
	nombre = models.CharField(max_length=200)
	latitud = models.DecimalField(max_digits=20, decimal_places=18)
	longitud = models.DecimalField(max_digits=20, decimal_places=18)
	descripcion = models.TextField(null=True)
	categorias = models.ManyToManyField(Categoria)
	municipio = models.ForeignKey(Municipio, related_name='sitios') 


class Foto(models.Model):
	URLfoto = models.FileField(upload_to='Fotos/')
	sitio=models.ForeignKey(Sitio, related_name='fotos')

