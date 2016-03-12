# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_auto_20160229_2210'),
        ('authentication_module', '0005_customuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name=b'user', related_name='user_set', to='auth.Permission', blank=True, help_text=b'Specific permissions for this user.', verbose_name=b'user permissions'),
        ),
    ]
