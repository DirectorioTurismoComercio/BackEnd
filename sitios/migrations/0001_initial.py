# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('URLfoto', models.FileField(upload_to=b'Fotos/')),
                ('tipo', models.CharField(default=b'P', max_length=2, choices=[(b'P', b'PRINCIPAL'), (b'F', b'FACHADA'), (b'I', b'INTERIOR'), (b'PR', b'PRODUCTOS')])),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.TextField(default=b'')),
                ('whatsapp', models.TextField(default=b'')),
                ('horariolocal', models.TextField(default=b'', blank=True)),
                ('web', models.TextField(default=b'')),
                ('latitud', models.DecimalField(max_digits=20, decimal_places=18)),
                ('longitud', models.DecimalField(max_digits=20, decimal_places=18)),
                ('descripcion', models.TextField(null=True)),
                ('correolocal', models.TextField(default=b'')),
                ('ubicacionlocal', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SitioCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(default=1)),
                ('categoria', models.ForeignKey(to='plataforma.Categoria')),
                ('sitio', models.ForeignKey(to='sitios.Sitio')),
            ],
        ),
        migrations.AddField(
            model_name='sitio',
            name='categorias',
            field=models.ManyToManyField(to='plataforma.Categoria', through='sitios.SitioCategoria'),
        ),
        migrations.AddField(
            model_name='sitio',
            name='municipio',
            field=models.ForeignKey(related_name='sitios', to='plataforma.Municipio'),
        ),
        migrations.AddField(
            model_name='sitio',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag'),
        ),
        migrations.AddField(
            model_name='sitio',
            name='usuario',
            field=models.ForeignKey(related_name='sitios', to='plataforma.Usuario'),
        ),
        migrations.AddField(
            model_name='foto',
            name='sitio',
            field=models.ForeignKey(related_name='fotos', to='sitios.Sitio'),
        ),
    ]
