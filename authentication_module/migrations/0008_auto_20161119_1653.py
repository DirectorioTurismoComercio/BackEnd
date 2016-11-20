# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0007_customuser_es_cuenta_activa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_cuenta',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'C', b'COMERCIANTE'), (b'M', b'MUNICIPIO'), (b'T', b'TURISTA')]),
        ),
    ]
