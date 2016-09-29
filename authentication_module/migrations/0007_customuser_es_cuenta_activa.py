# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0006_auto_20160831_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='es_cuenta_activa',
            field=models.BooleanField(default=True),
        ),
    ]
