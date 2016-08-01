# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0002_auto_20160801_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitio',
            old_name='user',
            new_name='usuario',
        ),
    ]
