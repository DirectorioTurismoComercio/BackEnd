# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='first_name',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='email',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='last_name',
            new_name='nombres',
        ),
    ]
