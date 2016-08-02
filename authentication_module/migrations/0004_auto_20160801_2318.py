# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0003_auto_20160801_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='apellidos',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='nombres',
            new_name='last_name',
        ),
    ]
