# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0010_auto_20160905_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='correolocal',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='telefono',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='tipo_sitio',
            field=models.CharField(default=b'S', max_length=1, null=True, blank=True, choices=[(b'M', b'MUNICIPIO'), (b'S', b'SITIO')]),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='ubicacionlocal',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='web',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='whatsapp',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
