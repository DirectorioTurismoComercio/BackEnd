from django.shortcuts import render
from social.apps.django_app.views import _do_login as social_auth_login
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_social_auth.views import BaseSocialAuthView 
from rest_social_auth.serializers import (OAuth2InputSerializer, OAuth1InputSerializer, UserSerializer,
    TokenSerializer, UserTokenSerializer, JWTSerializer, UserJWTSerializer)


class CustomSocialTokenUserAuthView(BaseSocialAuthView):
    serializer_class = UserTokenSerializer
    authentication_classes = (TokenAuthentication, )
    def do_login(self, backend, user):
       print("login...", user.username,"////",user.email, "***", self, "||", backend)

