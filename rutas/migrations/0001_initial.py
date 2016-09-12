# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0013_auto_20160905_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RutaSitio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField()),
                ('ruta', models.ForeignKey(to='rutas.Ruta')),
                ('sitio', models.ForeignKey(to='sitios.Sitio')),
            ],
        ),
        migrations.AddField(
            model_name='ruta',
            name='sitios',
            field=models.ManyToManyField(to='sitios.Sitio', through='rutas.RutaSitio'),
        ),
    ]
