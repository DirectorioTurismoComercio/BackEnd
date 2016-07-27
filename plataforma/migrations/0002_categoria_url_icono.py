# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='URL_icono',
            field=models.FileField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
