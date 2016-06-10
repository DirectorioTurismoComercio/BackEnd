from django.db import models

# Create your models here.

from django.db import models
from plataforma.models import Categoria
from plataforma.models import Municipio
from plataforma.models import Tag
from plataforma.models import Usuario


class Sitio(models.Model):
	nombre = models.CharField(max_length=200, null=False)
	telefono = models.IntegerField(default=0)
	whatsapp = models.IntegerField(default=0)
	horariolocal = models.TextField(default="")
	web = models.TextField(default="")
	latitud = models.DecimalField(max_digits=20, decimal_places=18, null=False)
	longitud = models.DecimalField(max_digits=20, decimal_places=18, null=False)
	descripcion = models.TextField(null=True)
	correolocal = models.TextField(default="")
	ubicacionlocal = models.TextField(null=True)
	categorias = models.ManyToManyField(Categoria)
	tags = models.ManyToManyField(Tag)
	usuario = models.ForeignKey(Usuario, related_name='sitios', null=False)
	municipio = models.ForeignKey(Municipio, related_name='sitios', null=False) 


class Foto(models.Model):
	URLfoto = models.FileField(upload_to='Fotos/')
	sitio=models.ForeignKey(Sitio, related_name='fotos')
	tipo = models.CharField(max_length=2,choices=(('P','PRINCIPAL'),('F','FACHADA'),('I','INTERIOR'),('PR','PRODUCTOS')),default='P',
                                                  null=False, blank=False)

