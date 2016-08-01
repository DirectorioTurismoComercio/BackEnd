# -*- encoding: utf-8 -*-
from django.db import models
from django.conf.urls import url
from django.contrib.auth.models import User
from authentication_module.models import *


## Modelo para representar una palabra o frase como Tag 
class Tag(models.Model):
    tag = models.CharField(max_length=255, null=False)


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    nivel = models.IntegerField(default=0)
    categoria_padre = models.ForeignKey("self",null=True) 
    URL_icono_normal = models.FileField(upload_to="normal_icons", null=True)
    URL_icono_seleccionado = models.FileField(upload_to="selected_iconos", null=True)


class Municipio(models.Model):
  nombre = models.TextField(null=False)
  latitud = models.DecimalField(max_digits=20, decimal_places=18)
  longitud = models.DecimalField(max_digits=20, decimal_places=18)


  
 



  
   








    