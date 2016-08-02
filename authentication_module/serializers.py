from rest_framework import serializers
from authentication_module.models import *
from sitios.serializers import SitioSerializer


class CustomUserSerializer(serializers.ModelSerializer):
	sitios = SitioSerializer(many=True, read_only=True) 
 	class Meta:
   		model = CustomUser
   		fields = ('id','email', 'password','first_name','last_name','sitios')
   		extra_kwargs = {'password': {'write_only': True}}
   		