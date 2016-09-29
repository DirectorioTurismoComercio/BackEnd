# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0005_auto_20160919_2225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rutasitio',
            options={'ordering': ('orden',)},
        ),
    ]
