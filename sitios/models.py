from django.db import models

# Create your models here.

from django.db import models

class Sitio(models.Model):
	nombre = models.CharField(max_length=200)
	latitud = models.DecimalField(max_digits=10, decimal_places=10)
	longitud = models.DecimalField(max_digits=10, decimal_places=10)



