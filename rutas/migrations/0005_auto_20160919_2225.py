# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0004_auto_20160915_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='distancia',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ruta',
            name='tiempo',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
