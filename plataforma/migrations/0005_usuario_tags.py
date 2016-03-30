# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_auto_20160330_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag'),
        ),
    ]
