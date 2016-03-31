# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.DecimalField(max_digits=10, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=10, decimal_places=10)),
            ],
        ),
    ]
