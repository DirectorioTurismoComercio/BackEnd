# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0002_auto_20160801_1950'),
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
