# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_remove_usuario_tags'),
        ('sitios', '0008_auto_20160513_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag'),
        ),
    ]
