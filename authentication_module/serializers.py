from rest_framework import serializers
from authentication_module.models import *
from sitios.serializers import SitioSerializer


class CustomUserSerializer(serializers.ModelSerializer):
	sitios = SitioSerializer(many=True, read_only=True) 
 	class Meta:
   		model = CustomUser
   		