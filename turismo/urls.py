from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from plataforma import views
from sitios import views as sitio_views
from rutas import views as ruta_views
from django.views.generic import RedirectView
from authentication_module import views as authentication_module_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

import local_settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^buscar/$', sitio_views.SitioList.as_view()), 
    url(r'^sugerencias/$', sitio_views.Sugerencias.as_view({'get':'list_sugerencias'})), 
    url(r'^municipios', views.MunicipiosListCreate.as_view()), 
    url(r'^municipio/sitios', sitio_views.SitiosDelMunicipio.as_view()), 
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
    url(r'^sitio/municipios', sitio_views.SitioMunicipioList.as_view()),
    url(r'^sitio/detail/(?P<pk>[0-9]+)', sitio_views.SitioDetail.as_view()), 
    url(r'^sitio', sitio_views.SitioCreate.as_view()), 
    url(r'^ruta/crear', ruta_views.RutaCreate.as_view()), 
    url(r'^ruta/actualizar/(?P<pk>[0-9]+)', ruta_views.RutaDetail.as_view()), 
    url(r'^rutas', ruta_views.RutaList.as_view()), 

     url(r'^admin/', include(admin.site.urls)), 
   
)
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns=urlpatterns+static(local_settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

