# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0004_auto_20160502_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='sitio',
            field=models.ForeignKey(related_name='fotos', to='sitios.Sitio'),
        ),
    ]
