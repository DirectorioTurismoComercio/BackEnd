from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

# Create your models here.

from django.db import models
from plataforma.models import Categoria
from plataforma.models import Municipio
from plataforma.models import Tag

from authentication_module.models import CustomUser

from django.core.validators import RegexValidator

from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser



class Sitio(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    telefono = models.TextField(default="",blank=True)
    whatsapp = models.TextField(default="",blank=True)
    horariolocal = models.TextField(default="", blank=True)
    businessOpenningHours = models.TextField(default="", blank=True)
    web = models.TextField(default="",null=True,blank=True)
    latitud = models.DecimalField(max_digits=20, decimal_places=18, null=False)
    longitud = models.DecimalField(max_digits=20, decimal_places=18, null=False)
    descripcion = models.TextField(null=True)
    description = models.TextField(null=True, blank=True)
    correolocal = models.TextField(default="",blank=True)
    ubicacionlocal = models.TextField(null=True,blank=True)
    categorias = models.ManyToManyField(Categoria, through='SitioCategoria')
    tags = models.ManyToManyField(Tag,blank=True)
    usuario = models.ForeignKey(CustomUser,null=True,related_name='sitios')
    municipio = models.ForeignKey(Municipio, related_name='sitios', null=False)
    tipo_sitio =  models.CharField(max_length=1,choices=(('M','MUNICIPIO'),('S','SITIO')),default='S',                                                  null=True, blank=True)
    calificacionPromedio = models.DecimalField(max_digits=3, decimal_places=2, null=True, default=None)
    votos = models.IntegerField(default=0)
    def __unicode__(self):
        return self.nombre



class Foto(models.Model):
    URLfoto = models.FileField(upload_to='Fotos/')
    sitio=models.ForeignKey(Sitio, related_name='fotos')
    tipo = models.CharField(max_length=2,choices=(('P','PRINCIPAL'),('F','FACHADA'),('I','INTERIOR'),('PR','PRODUCTOS')),default='P',
                                                  null=False, blank=False)
	


@receiver(pre_delete, sender=Foto)
def Foto_delete(sender, instance, **kwargs):
    instance.URLfoto.delete(False)

class SitioCategoria(models.Model):
    tipo = models.IntegerField(default=1)
    categoria = models.ForeignKey(Categoria,blank=False)
    sitio = models.ForeignKey(Sitio,blank=False)


class Calificacion(models.Model):
    user = models.ForeignKey(CustomUser)
    sitio = models.ForeignKey(Sitio)
    calificacion = models.IntegerField(default=1)