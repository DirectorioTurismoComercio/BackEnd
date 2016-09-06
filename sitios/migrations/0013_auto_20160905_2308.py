# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0012_auto_20160905_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='tags',
            field=models.ManyToManyField(to='plataforma.Tag', blank=True),
        ),
    ]
