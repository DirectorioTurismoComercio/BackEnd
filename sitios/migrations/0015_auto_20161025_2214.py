# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0014_sitio_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
