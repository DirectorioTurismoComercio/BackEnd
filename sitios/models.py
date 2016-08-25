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
	telefono = models.TextField(default="")
	whatsapp = models.TextField(default="")
	horariolocal = models.TextField(default="", blank=True)
	web = models.TextField(default="")
	latitud = models.DecimalField(max_digits=20, decimal_places=18, null=False)
	longitud = models.DecimalField(max_digits=20, decimal_places=18, null=False)
	descripcion = models.TextField(null=True)
	correolocal = models.TextField(default="")
	ubicacionlocal = models.TextField(null=True)
	categorias = models.ManyToManyField(Categoria, through='SitioCategoria')
	tags = models.ManyToManyField(Tag)
	usuario = models.ForeignKey(CustomUser,null=True,related_name='sitios')
	municipio = models.ForeignKey(Municipio, related_name='sitios', null=False) 


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


class AppUser():
	_SEX = (
	    ('M', 'Male'),
	    ('F', 'Female'),
	)
	_pregex  = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone    = models.CharField(validators=[_pregex], max_length=16, blank=True)
	gender   = models.CharField(max_length=1, blank=True, null=True, choices=_SEX)
	birthday = models.DateField(blank=True, null=True)
	vericode = models.CharField(max_length=40, blank=True, null=True) # verification code over SMS?
	verified = models.DateTimeField(null=True, blank=True) # datetime stored when verification happened

	# for DJOSER
	# define required fields here, so you can call put /auth/me to update your profile
	REQUIRED_FIELDS = User.REQUIRED_FIELDS + ['first_name', 'last_name', 'gender', 'birthday']

	@property
	def age(self):
	    if self.birthday:
	        today = date.today()
	        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
	    return None