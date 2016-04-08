# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0007_auto_20160404_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipio',
            name='URLfoto',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='descripcion',
        ),
    ]
