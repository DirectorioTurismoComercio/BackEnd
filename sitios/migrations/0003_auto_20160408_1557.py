# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0002_auto_20160404_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='URLfoto',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sitio',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
