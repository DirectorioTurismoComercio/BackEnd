# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0017_calificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='calificacionPromedio',
            field=models.DecimalField(default=None, null=True, max_digits=1, decimal_places=1),
        ),
        migrations.AddField(
            model_name='sitio',
            name='votos',
            field=models.IntegerField(default=0),
        ),
    ]
