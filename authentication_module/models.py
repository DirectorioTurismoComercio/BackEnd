from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class CustomUser(AbstractBaseUser):
	username = models.CharField(max_length=30, blank=True)
	email = models.EmailField(unique=True)
	USERNAME_FIELD = 'email'
	objects = UserManager()