# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0006_auto_20160404_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='URLfoto',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
