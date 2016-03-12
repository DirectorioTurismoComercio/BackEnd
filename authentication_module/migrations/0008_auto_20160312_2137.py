# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0007_customuser_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
