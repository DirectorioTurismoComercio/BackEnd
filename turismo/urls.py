from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from plataforma import views
from sitios import views as sitio_views
from django.views.generic import RedirectView
from authentication_module import views as authentication_module_views


urlpatterns = patterns('',
    # Examples:   //
    url(r'^buscar/$', sitio_views.SitioListCreate.as_view()), 
    url(r'^sugerencias/$', sitio_views.Sugerencias.as_view({'get':'list_sugerencias'})), 
   #url(r'^sugerencias_tags/$', views.Sugerencias.as_view({'get':'list_sugerencias_tags'})), 
    url(r'^municipios', views.MunicipiosListCreate.as_view()), 
    url(r'^usuarios', views.UsuarioListCreate.as_view()), 
    url(r'^usuario', views.UsuarioDetail.as_view()),
    url(r'^categorias/(?P<pk>[0-9]+)', views.CategoriaDetail.as_view()),
    url(r'^categorias', views.CategoriaListCreate.as_view()), 
    url(r'^tags/(?P<pk>[0-9]+)', views.TagDetail.as_view()),
    url(r'^tags', views.TagListCreate.as_view()), 
    url(r'^docs/', include('rest_framework_swagger.urls')), # url documentation
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/'), name='profile-redirect'),
    url(r'^api/login/social/token/(?:(?P<provider>[a-zA-Z0-9_-]+)/?)?$',
       authentication_module_views.CustomSocialTokenUserAuthView.as_view(),
        name='login_social_token_user'),
    url(r'^ruta/sitios', sitio_views.SitiosCercanosARuta.as_view({'post':'list_sites'})), 

   
)
urlpatterns = format_suffix_patterns(urlpatterns)