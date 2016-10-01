# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_categoria_url_icono_general'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='name',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
    ]
