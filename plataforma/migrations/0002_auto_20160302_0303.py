# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido2',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
