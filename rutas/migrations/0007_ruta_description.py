# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0006_auto_20160926_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
