# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_auto_20160316_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido1',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='NIT',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido2',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo_institucion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion_institucion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='municipio_id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre_institucion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='numero_documento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='redes',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono_institucion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='ubicacion_institucion',
        ),
    ]
