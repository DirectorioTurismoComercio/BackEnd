from rest_framework import serializers
from authentication_module.models import *
from sitios.serializers import SitioSerializer
from social.apps.django_app.default.models import UserSocialAuth


class UserSocialAuthSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserSocialAuth
		fields = ('provider',)

class CustomUserSerializer(serializers.ModelSerializer):
	sitios = SitioSerializer(many=True, read_only=True) 
	social_auth = UserSocialAuthSerializer(many=True,read_only=True)
 	class Meta:
   		model = CustomUser
   		fields = ('id','email', 'first_name','last_name','sitios','social_auth')
   		
   		