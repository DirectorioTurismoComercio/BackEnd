# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0015_auto_20161025_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='businessOpenningHours',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
