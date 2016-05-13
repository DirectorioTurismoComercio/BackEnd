# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_auto_20160408_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tags',
        ),
    ]
