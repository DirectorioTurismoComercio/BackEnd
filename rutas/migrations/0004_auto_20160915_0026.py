# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0003_auto_20160914_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ruta',
            old_name='municipio',
            new_name='sitio',
        ),
    ]
