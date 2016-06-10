# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0011_sitio_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='tipo',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'P', b'PRINCIPAL'), (b'F', b'FACHADA'), (b'I', b'INTERIOR'), (b'PR', b'PRODUCTOS')]),
        ),
        migrations.AddField(
            model_name='sitio',
            name='web',
            field=models.TextField(default=b''),
        ),
    ]
