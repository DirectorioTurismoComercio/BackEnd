from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from plataforma import views
from django.views.generic import RedirectView
from authentication_module import views as authentication_module_views
# from landing_page import views

urlpatterns = patterns('',
    # Examples:   //
    url(r'^roles/cuestionarios', views.RolCuestionariosSave.as_view({'post':'create'})), 
    url(r'^roles/(?P<pk>[0-9]+)/cuestionarios', views.RolCuestionariosRetrieve.as_view()), 
    url(r'^roles/(?P<pk>[0-9]+)', views.RolDetail.as_view()),  
    url(r'^roles/', views.RolListCreate.as_view()),
    url(r'^usuariosredes/(?P<pk>[0-9]+)', views.UsuarioRedesDetail.as_view()),
    url(r'^usuariosredes', views.UsuarioRedesListCreate.as_view()),
    url(r'^usuarios/(?P<usuario>[0-9]+)/problemas_soluciones/(?P<pk>[0-9]+)', views.ProblemaSolucionDetail.as_view()),
    url(r'^usuarios/(?P<usuario>[0-9]+)/problemas_soluciones', views.ProblemaSolucionListCreate.as_view()), 

    url(r'^buscar/$', views.ProblemaSolucionListCreate.as_view()), 
    url(r'^sugerencias/$', views.Sugerencias.as_view({'get':'list_sugerencias'})), 
    url(r'^sugerencias_tags/$', views.Sugerencias.as_view({'get':'list_sugerencias_tags'})), 
    url(r'^usuario/(?P<usuario>[0-9]+)/busquedas', views.ProblemaSolucionListCreate.as_view()), 
    url(r'^usuario/(?P<usuario>[0-9]+)/busquedas', views.BusquedaCreateRetrieve.as_view({'post':'create'})), 
    url(r'^usuario/(?P<usuario>[0-9]+)/conversaciones', views.ConversacionView.as_view({'get':'list'})), 
    
    url(r'^conversaciones/mensaje', views.ConversacionView.as_view({'post':'create_message'})), 
    url(r'^conversacion/(?P<pk>[0-9]+)', views.ConversacionView.as_view({'get':'get_conversation_pk'})), 
    
    url(r'^conversacion', views.ConversacionView.as_view({'get':'get_conversation'})), 

    url(r'^mensaje/leido/(?P<pk>[0-9]+)', views.ConversacionView.as_view({'put':'message_read'})), 
    
    url(r'^municipios', views.MunicipiosView.as_view({'get':'list'})), 
   
    url(r'^usuarios/(?P<pk>[0-9]+)/redes', views.UsuarioRedesList.as_view()),  
    url(r'^usuarios', views.UsuarioListCreate.as_view()), 
    url(r'^usuario', views.UsuarioDetail.as_view()),
    url(r'^redes/(?P<pk>[0-9]+)', views.RedSocialDetail.as_view()),
    url(r'^redes', views.RedSocialListCreate.as_view()),
    url(r'^categorias/(?P<pk>[0-9]+)', views.CategoriaDetail.as_view()),
    url(r'^categorias', views.CategoriaListCreate.as_view()), 
    url(r'^problemas_soluciones/(?P<pk>[0-9]+)', views.ProblemaSolucionDetail.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)', views.TagDetail.as_view()),
    url(r'^tags', views.TagListCreate.as_view()), 
    url(r'^cuestionarios/(?P<pk>[0-9]+)', views.CuestionarioRetrieve.as_view()), 
    url(r'^cuestionarios', views.CuestionarioList.as_view()), 
    url(r'^afinidad/detalle', views.AfinidadList.as_view({'post':'detail'})), 
    url(r'^afinidad', views.AfinidadList.as_view({'post':'list'})), 
  
    

    url(r'^respuestas/busqueda/(?P<pk>[0-9]+)', views.RespuestaProblemaSolucionDetail.as_view()),
    url(r'^respuestas/busqueda', views.RespuestaProblemaSolucionCreate.as_view()),
    url(r'^busqueda/(?P<pk>[0-9]+)', views.BusquedaCreateRetrieve.as_view({'get':'get'})),
    url(r'^docs/', include('rest_framework_swagger.urls')), # url documentation

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/'), name='profile-redirect'),
    url(r'^api/login/social/token/(?:(?P<provider>[a-zA-Z0-9_-]+)/?)?$',
       authentication_module_views.CustomSocialTokenUserAuthView.as_view(),
        name='login_social_token_user'),
    

   
)
urlpatterns = format_suffix_patterns(urlpatterns)