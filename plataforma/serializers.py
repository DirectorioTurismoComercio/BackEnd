# coding=utf-8 

from django.forms import widgets
from rest_framework import serializers
from plataforma import models
from plataforma.models import Usuario
from plataforma.models import Rol
from plataforma.models import UsuarioRedes
from plataforma.models import RedSocial
from plataforma.models import Categoria
from plataforma.models import ProblemaSolucion
from plataforma.models import RespuestaProblemaSolucion
from plataforma.models import Tag
from plataforma.models import Cuestionario
from plataforma.models import CuestionarioPregunta
from plataforma.models import Pregunta
from plataforma.models import OpcionesDeRespuesta
from plataforma.models import CuestionarioRol
from plataforma.models import ProblemaSolucionOpcionRespuesta
from plataforma.models import Conversacion
from plataforma.models import Mensaje
from django.contrib.auth.models import User

# Serializador del modelo User de django.contrib.auth.models
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('email', 'password')
 
# Serializador del modelo RedSocial
class RedSocialSerializer(serializers.ModelSerializer):  
        class Meta:
            model = RedSocial      

# Serializador del modelo UsuarioRedes
class UsuarioRedesSerializer(serializers.ModelSerializer):
        class Meta:
            model = UsuarioRedes

# Serializador del modelo Rol

class RolSerializer(serializers.ModelSerializer):
   class Meta:
        model = Rol       

# Serializador de los Municipios para el registro y para las preguntas. Corresponde al nodelo OpcionesDeRespuesta
class MunicipiosSerializer(serializers.ModelSerializer):
  nombre = serializers.CharField(source='respuesta')
  class Meta:
        model = OpcionesDeRespuesta 
        fields = ('id','nombre')    
              
# Serializador del modelo Usuario      
class UsuarioSerializer(serializers.ModelSerializer):
   tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False)
    
   def to_internal_value(self, data):
      if data.get("tags") is not None:   # si existen tags
        self.check_for_new_tags(data.get("tags")) #entonces revisa cuales tags son nuevos
      return super(UsuarioSerializer,self).to_internal_value(data)

   def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan 
      for tag in tags:
        try:
             tag_object = Tag.objects.get(tag=tag)
        except:
             tag_object = Tag.objects.create(tag=tag)   
   class Meta:
        model = Usuario

# Serializador del modelo Categoría
class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Categoria

# Serializador del modelo ProblemaSolucion, no incluye todos los campos.
class RespuestaProblemaSolucionAsociadaSerializer(serializers.ModelSerializer):
   class Meta:
        model = ProblemaSolucion
        fields =('id','titulo','descripcion','fecha','tipo','usuario')


# Serializador del modelo RespuestaProblema
class RespuestaProblemaSerializer(serializers.ModelSerializer):
   id_busqueda_respuesta= serializers.IntegerField(source='id',read_only=True)
   problema_solucion = RespuestaProblemaSolucionAsociadaSerializer(read_only=True,source='respuesta')
 
   class Meta:
        model = RespuestaProblemaSolucion  
        fields =('id_busqueda_respuesta','problema_solucion')

# Serializador del modelo ProblemaSolucion, incluye todos los campos.
class ProblemaSolucionSerializer(serializers.Serializer):
  
  id = serializers.IntegerField(read_only=True)   
  titulo = serializers.CharField(max_length=200)
  descripcion =serializers.CharField()
  fecha = serializers.DateTimeField(required=False, allow_null=True)
  tipo = serializers.ChoiceField([('P','PROBLEMA'),('S','SOLUCION')])
  respuestas_cuestionario = serializers.CharField()
  tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag',required=True)
  usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
  categorias = serializers.PrimaryKeyRelatedField(many=True, queryset=Categoria.objects.all(), required=True)
  categorias_completas = CategoriaSerializer(many=True,read_only=True, source="categorias")
  #respuestas_asociadas = RespuestaProblemaSerializer(source='busqueda',many=True)
  # respuestas_asociadas = RespuestaProblemaSerializer(many=True,read_only=True)
  #respuesta = serializers.Forein

  def to_internal_value(self, data):
        if data.get("tags") is not None:   # si existen tags
          self.check_for_new_tags(data.get("tags")) #entonces revisa cuales tags son nuevos
        return super(ProblemaSolucionSerializer,self).to_internal_value(data)

  def create(self, validated_data):  
      instance=ProblemaSolucion.objects.create(titulo=validated_data["titulo"],
        descripcion=validated_data["descripcion"],
        tipo=validated_data["tipo"],
        respuestas_cuestionario=validated_data["respuestas_cuestionario"],
        usuario=validated_data["usuario"]
        );
      instance.categorias = validated_data["categorias"]
      instance.tags = validated_data["tags"]
      instance.save()
      return instance

  def update(self, instance, validated_data):
      instance.titulo = validated_data.get('titulo', instance.titulo)
      instance.descripcion = validated_data.get('descripcion', instance.descripcion)
      instance.fecha = validated_data.get('fecha', instance.fecha)
      instance.tipo = validated_data.get('tipo', instance.tipo) 
      instance.categorias = validated_data.get('categorias', instance.categorias)
      instance.tags = validated_data.get('tags', instance.tags)
      instance.usuario = validated_data.get('usuario', instance.usuario)
      instance.respuestas_cuestionario = validated_data.get('respuestas_cuestionario', instance.respuestas_cuestionario)
      instance.save()
      return instance

  def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan
    if tags is not None:
      for tag in tags:
        
        try:
             tag_object = Tag.objects.get(tag=tag)
        except:
             tag_object = Tag.objects.create(tag=tag)
         
 # Serializador del modelo RespuestaProblemaSolucion
class RespuestaProblemaSolucionSerializer(serializers.ModelSerializer):
   class Meta:
        model = RespuestaProblemaSolucion

# Serializador del modelo Tag
class TagSerializer(serializers.ModelSerializer):
   class Meta:
        model = Tag

# Serializador del modelo OpcionesDeRespuesta
class OpcionesDeRespuestaSerializer(serializers.ModelSerializer,serializers.Serializer):
  class Meta:
        model = OpcionesDeRespuesta
        

# Serializador del modelo Pregunta
class PreguntaSerializer(serializers.ModelSerializer):
   opciones = OpcionesDeRespuestaSerializer(many=True,read_only=True) 
   class Meta:
        model = Pregunta
        
# Serializador del modelo CuestionarioPregunta
class CuestionarioPreguntaSerializer(serializers.ModelSerializer):
  pregunta = PreguntaSerializer()
  class Meta:
    model = CuestionarioPregunta

  
# Serializador del modelo Cuestionario
class CuestionarioSerializer(serializers.ModelSerializer): 
   preguntas = CuestionarioPreguntaSerializer(source='cuestionariopregunta_set', many=True)  
   class Meta:
        model = Cuestionario      
        depth=4     

# Serializador del modelo ProblemaSolucionOpcionRespuesta
class CuestionarioRolSerializer(serializers.ModelSerializer):
  cuestionario = CuestionarioSerializer()
  class Meta:
    model = CuestionarioRol

# Serializador del modelo Cuestionario
class ProblemaSolucionOpcionRespuestaSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProblemaSolucionOpcionRespuesta    

# Serializador del modelo Conversación

class ConversacionSerializer(serializers.ModelSerializer):
  busqueda = ProblemaSolucionSerializer()
  respuesta = ProblemaSolucionSerializer()
  class Meta:
    model = Conversacion
 
 # Serializador del modelo Mensaje
class MensajeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mensaje

# Serializador del modelo conversación.
class ConversacionMensajesSerializer(serializers.ModelSerializer):
  busqueda = ProblemaSolucionSerializer()
  respuesta = ProblemaSolucionSerializer()
  mensajes = MensajeSerializer(many=True)
  class Meta:
    model = Conversacion   


