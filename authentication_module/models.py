from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group


from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext as _



class CustomUser(AbstractBaseUser, PermissionsMixin):
	REQUIRED_FIELDS = [] 
	username = models.CharField(max_length=30, blank=True)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(unique=True)
	is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
	is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	tipo_cuenta = models.CharField(max_length=1,choices=(('C','COMERCIANTE'),('M','MUNICIPIO'),('T','TURISTA')),
                                                  null=True, blank=True)
	es_cuenta_activa = models.BooleanField(default=True)
	USERNAME_FIELD = 'email'
	objects = UserManager()

