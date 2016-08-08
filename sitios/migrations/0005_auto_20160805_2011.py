# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0004_auto_20160801_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='tipo',
            field=models.CharField(default=b'Z', max_length=2, choices=[(b'Z', b'PRINCIPAL'), (b'F', b'FACHADA'), (b'I', b'INTERIOR'), (b'PR', b'PRODUCTOS')]),
        ),
    ]
