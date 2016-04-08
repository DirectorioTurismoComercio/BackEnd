# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='latitud',
            field=models.DecimalField(max_digits=20, decimal_places=18),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='longitud',
            field=models.DecimalField(max_digits=20, decimal_places=18),
        ),
    ]
