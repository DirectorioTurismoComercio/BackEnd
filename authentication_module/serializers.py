from rest_framework import serializers
from authentication_module.models import *

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('email', 'password')