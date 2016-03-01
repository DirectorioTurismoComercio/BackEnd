# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_auto_20160229_2353'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
