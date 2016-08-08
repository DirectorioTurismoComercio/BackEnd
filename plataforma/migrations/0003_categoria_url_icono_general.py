# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_auto_20160801_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='URL_icono_general',
            field=models.FileField(null=True, upload_to=b'general_icons'),
        ),
    ]
