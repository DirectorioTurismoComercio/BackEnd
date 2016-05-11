# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_auto_20160408_1557'),
        ('sitios', '0006_sitio_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='municipio',
            field=models.ForeignKey(related_name='sitios', default=1, to='plataforma.Municipio'),
            preserve_default=False,
        ),
    ]
