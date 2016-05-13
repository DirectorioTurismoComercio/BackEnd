# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0007_sitio_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='correolocal',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='sitio',
            name='horariolocal',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='sitio',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sitio',
            name='ubicacionlocal',
            field=models.TextField(null=True),
        ),
    ]
