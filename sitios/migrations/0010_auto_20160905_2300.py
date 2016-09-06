# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0009_sitio_tipo_sitio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='web',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='whatsapp',
            field=models.TextField(default=b'', null=True),
        ),
    ]
