# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0013_auto_20160905_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
