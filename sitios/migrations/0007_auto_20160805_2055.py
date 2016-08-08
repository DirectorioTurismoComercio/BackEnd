# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0006_auto_20160805_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='tipo',
            field=models.CharField(default=b'P', max_length=2, choices=[(b'C', b'PRINCIPAL'), (b'F', b'FACHADA'), (b'I', b'INTERIOR'), (b'PR', b'PRODUCTOS')]),
        ),
    ]
