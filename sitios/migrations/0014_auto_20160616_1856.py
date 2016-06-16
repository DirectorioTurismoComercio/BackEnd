# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0013_auto_20160610_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='telefono',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='whatsapp',
            field=models.TextField(default=b''),
        ),
    ]
