# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_auto_20160229_2210'),
        ('authentication_module', '0006_customuser_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(related_query_name=b'user', related_name='user_set', to='auth.Group', blank=True, help_text=b'The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name=b'groups'),
        ),
    ]
