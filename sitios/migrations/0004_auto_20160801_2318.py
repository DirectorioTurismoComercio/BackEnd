# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0003_auto_20160801_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='usuario',
            field=models.ForeignKey(related_name='sitios', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
