# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0018_auto_20161119_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='calificacionPromedio',
            field=models.DecimalField(default=None, null=True, max_digits=3, decimal_places=2),
        ),
    ]
