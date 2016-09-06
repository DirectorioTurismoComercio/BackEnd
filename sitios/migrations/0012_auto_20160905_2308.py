# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0011_auto_20160905_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag', null=True, blank=True),
        ),
    ]
