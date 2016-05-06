# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_auto_20160408_1557'),
        ('sitios', '0005_auto_20160504_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='categorias',
            field=models.ManyToManyField(to='plataforma.Categoria'),
        ),
    ]
