from django.db import models

# Create your models here.

from django.db import models

class Sitio(models.Model):
	nombre = models.CharField(max_length=200)
	latitud = models.DecimalField(max_digits=20, decimal_places=18)
	longitud = models.DecimalField(max_digits=20, decimal_places=18)
	descripcion = models.TextField(null=True)

class Foto(models.Model):
	URLfoto = models.FileField(upload_to='Fotos/')
	sitio=models.ForeignKey(Sitio, related_name='fotos')

