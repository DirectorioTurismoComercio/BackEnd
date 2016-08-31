# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0005_customuser_tipo_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_cuenta',
            field=models.CharField(default=b'C', max_length=1, null=True, blank=True, choices=[(b'C', b'COMERCIANTE'), (b'M', b'MUNICIPIO')]),
        ),
    ]
