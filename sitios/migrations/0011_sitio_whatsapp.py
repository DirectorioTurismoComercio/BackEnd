# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0010_sitio_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='whatsapp',
            field=models.IntegerField(default=0),
        ),
    ]
