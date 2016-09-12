# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_categoria_url_icono_general'),
        ('rutas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='municipio',
            field=models.ForeignKey(default=1, to='plataforma.Municipio'),
            preserve_default=False,
        ),
    ]
