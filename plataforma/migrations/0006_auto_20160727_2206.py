# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_auto_20160727_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='URL_icono',
        ),
        migrations.AddField(
            model_name='categoria',
            name='URL_icono_normal',
            field=models.FileField(null=True, upload_to=b'normal_icons'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='URL_icono_seleccionado',
            field=models.FileField(null=True, upload_to=b'selected_iconos'),
        ),
    ]
