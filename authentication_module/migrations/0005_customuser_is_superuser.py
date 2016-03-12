# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0004_auto_20160312_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
