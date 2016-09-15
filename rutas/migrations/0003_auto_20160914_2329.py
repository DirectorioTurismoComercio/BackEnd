# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0002_ruta_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='municipio',
            field=models.ForeignKey(related_name='rutas', to='sitios.Sitio'),
        ),
    ]
