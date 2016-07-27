# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_auto_20160727_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='URL_icono',
            field=models.FileField(null=True, upload_to=b'iconos'),
        ),
    ]
