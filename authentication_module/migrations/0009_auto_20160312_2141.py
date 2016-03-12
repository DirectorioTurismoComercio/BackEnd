# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0008_auto_20160312_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date joined'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text=b'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name=b'active'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text=b'Designates whether the user can log into this admin site.', verbose_name=b'staff status'),
        ),
    ]
