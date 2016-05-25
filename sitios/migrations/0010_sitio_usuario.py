# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_remove_usuario_tags'),
        ('sitios', '0009_sitio_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='usuario',
            field=models.ForeignKey(related_name='sitios', default=1, to='plataforma.Usuario'),
            preserve_default=False,
        ),
    ]
