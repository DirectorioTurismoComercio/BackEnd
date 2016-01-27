# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('nivel', models.IntegerField(default=0)),
                ('categoria_padre', models.ForeignKey(to='plataforma.Categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('imagen', models.CharField(max_length=200, null=True, blank=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CuestionarioPregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField()),
                ('cuestionario', models.ForeignKey(to='plataforma.Cuestionario')),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='CuestionarioRol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField()),
                ('tipo', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PROBLEMA'), (b'S', b'SOLUCION')])),
                ('cuestionario', models.ForeignKey(to='plataforma.Cuestionario')),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.TextField(null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('visto', models.BooleanField(default=False)),
                ('conversacion', models.ForeignKey(related_name='mensajes', to='plataforma.Conversacion')),
            ],
        ),
        migrations.CreateModel(
            name='OpcionesDeRespuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=200, null=True)),
                ('orden', models.IntegerField()),
                ('valor', models.CharField(max_length=200, null=True)),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enunciado', models.CharField(max_length=200, null=True)),
                ('imagen', models.CharField(max_length=200, null=True, blank=True)),
                ('tipo_pregunta', models.CharField(default=b'U', max_length=1, choices=[(b'U', b'UNICA RESPUESTA'), (b'M', b'MULTIPLE RESPUESTA'), (b'L', b'LISTA')])),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasSimilitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemaSolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('tipo', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PROBLEMA'), (b'S', b'SOLUCION')])),
                ('respuestas_cuestionario', models.CharField(max_length=255, null=True)),
                ('categorias', models.ManyToManyField(to='plataforma.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemaSolucionOpcionRespuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opcion_respuesta', models.ForeignKey(to='plataforma.OpcionesDeRespuesta')),
                ('problema_solucion', models.ForeignKey(to='plataforma.ProblemaSolucion')),
            ],
        ),
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('icono', models.CharField(default=None, max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaProblemaSolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
                ('fecha', models.DateTimeField()),
                ('tipo', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PROBLEMA'), (b'S', b'SOLUCION')])),
                ('busqueda', models.ForeignKey(related_name='busqueda', to='plataforma.ProblemaSolucion')),
                ('respuesta', models.ForeignKey(related_name='respuesta', to='plataforma.ProblemaSolucion', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200, null=True, blank=True)),
                ('imagen', models.CharField(max_length=200, null=True, blank=True)),
                ('tipo_rol', models.CharField(default=b'BC', max_length=2, choices=[(b'BC', b'Busca en comercio'), (b'BT', b'Turismo'), (b'O', b'Ofrece')])),
                ('cuestionarios', models.ManyToManyField(to='plataforma.Cuestionario', through='plataforma.CuestionarioRol')),
            ],
        ),
        migrations.CreateModel(
            name='Similitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funcion', models.CharField(max_length=50, null=True)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=200)),
                ('apellido1', models.CharField(max_length=200)),
                ('apellido2', models.CharField(max_length=200)),
                ('numero_documento', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('correo', models.CharField(default=None, max_length=200, unique=True, null=True, blank=True)),
                ('nombre_institucion', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('telefono_institucion', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('ubicacion_institucion', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('direccion_institucion', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('correo_institucion', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('NIT', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('descripcion', models.TextField(null=True)),
                ('municipio_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioRedes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('red_social', models.ForeignKey(to='plataforma.RedSocial')),
                ('usuario', models.ForeignKey(to='plataforma.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variable', models.CharField(max_length=200)),
                ('valor', models.IntegerField()),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='redes',
            field=models.ManyToManyField(to='plataforma.RedSocial', through='plataforma.UsuarioRedes'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(to='plataforma.Rol'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='problemasolucion',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag'),
        ),
        migrations.AddField(
            model_name='problemasolucion',
            name='usuario',
            field=models.ForeignKey(to='plataforma.Usuario'),
        ),
        migrations.AddField(
            model_name='preguntassimilitud',
            name='funcion',
            field=models.ForeignKey(to='plataforma.Similitud'),
        ),
        migrations.AddField(
            model_name='preguntassimilitud',
            name='pregunta_A',
            field=models.ForeignKey(related_name='pregunta_problema', to='plataforma.Pregunta'),
        ),
        migrations.AddField(
            model_name='preguntassimilitud',
            name='pregunta_B',
            field=models.ForeignKey(related_name='pregunta_solucion', to='plataforma.Pregunta'),
        ),
        migrations.AddField(
            model_name='opcionesderespuesta',
            name='pregunta',
            field=models.ForeignKey(related_name='opciones', to='plataforma.Pregunta'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='destinatario',
            field=models.ForeignKey(related_name='usuario_destinatario', to='plataforma.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='usuario_busqueda',
            field=models.ForeignKey(related_name='usuario_busqueda', to='plataforma.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='usuario_respuesta',
            field=models.ForeignKey(related_name='usuario_respuesta', to='plataforma.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='cuestionariorol',
            name='rol',
            field=models.ForeignKey(to='plataforma.Rol'),
        ),
        migrations.AddField(
            model_name='cuestionariopregunta',
            name='dependencia_respuestas',
            field=models.ManyToManyField(to='plataforma.OpcionesDeRespuesta'),
        ),
        migrations.AddField(
            model_name='cuestionariopregunta',
            name='pregunta',
            field=models.ForeignKey(to='plataforma.Pregunta'),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='preguntas',
            field=models.ManyToManyField(to='plataforma.Pregunta', through='plataforma.CuestionarioPregunta'),
        ),
        migrations.AddField(
            model_name='conversacion',
            name='busqueda',
            field=models.ForeignKey(related_name='busqueda_', to='plataforma.ProblemaSolucion'),
        ),
        migrations.AddField(
            model_name='conversacion',
            name='respuesta',
            field=models.ForeignKey(related_name='respuesta_', to='plataforma.ProblemaSolucion', null=True),
        ),
    ]
