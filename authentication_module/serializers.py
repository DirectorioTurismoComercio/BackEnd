from rest_framework import serializers
from authentication_module.models import *
from sitios.serializers import SitioSerializer
from social.apps.django_app.default.models import UserSocialAuth
from django.core.exceptions import ValidationError


class UserSocialAuthSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserSocialAuth
		fields = ('provider',)

class CustomUserSerializer(serializers.ModelSerializer):
	sitios = SitioSerializer(many=True, read_only=True) 
	social_auth = UserSocialAuthSerializer(many=True,read_only=True)
	def is_valid(self, raise_exception=False):
		assert not hasattr(self, 'restore_object'), (
		    'Serializer `%s.%s` has old-style version 2 `.restore_object()` '
		    'that is no longer compatible with REST framework 3. '
		    'Use the new-style `.create()` and `.update()` methods instead.' %
		    (self.__class__.__module__, self.__class__.__name__)
		)

		assert hasattr(self, 'initial_data'), (
		    'Cannot call `.is_valid()` as no `data=` keyword argument was '
		    'passed when instantiating the serializer instance.'
		)

		if not hasattr(self, '_validated_data'):
			try:
				self._validated_data = self.run_validation(self.initial_data)
			except Exception as exc:
			    self._validated_data = {}
			    self._errors = exc.detail
			    
			    if 'email' in self._errors:
			    	if 'unique' in self._errors['email'][0]:
			    		self._errors['email'][0]='E101'
			    
			    
			    raise exc
			else:
				self._errors = {}

		if self._errors and raise_exception:
			raise ValidationError(self._errors)

		return not bool(self._errors)


 	class Meta:
   		model = CustomUser
   		fields = ('id','email', 'first_name','last_name','tipo_cuenta', 'sitios','social_auth')
   		
   		