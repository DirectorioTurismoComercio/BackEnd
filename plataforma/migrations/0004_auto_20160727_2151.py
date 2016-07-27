# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_auto_20160727_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='URL_icono',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/media/photos'), null=True, upload_to=b''),
        ),
    ]
