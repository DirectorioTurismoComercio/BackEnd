# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0004_auto_20160801_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tipo_cuenta',
            field=models.CharField(default=b'C', max_length=1, choices=[(b'C', b'COMERCIANTE'), (b'M', b'MUNICIPIO')]),
        ),
    ]
