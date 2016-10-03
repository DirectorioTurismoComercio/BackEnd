# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_categoria_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificador', models.CharField(default=b'MCI', max_length=3, null=True, blank=True, choices=[(b'MCA', b'MENSAJE_CUENTA_ACTIVA'), (b'MCI', b'MENSAJE_CUENTA_INACTIVA'), (b'MRC', b'MENSAJE_RECUPERAR_CONSTRASENA')])),
                ('asunto', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
            ],
        ),
    ]
