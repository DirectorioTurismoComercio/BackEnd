# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0008_auto_20160808_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='tipo_sitio',
            field=models.CharField(default=b'S', max_length=1, null=True, blank=True, choices=[(b'M', b'MUNICIPIO'), (b'S', b'SITIO'), (b'I', b'INTERIOR'), (b'PR', b'PRODUCTOS')]),
        ),
    ]
