# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0003_auto_20160408_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('URLfoto', models.FileField(upload_to=b'Fotos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='sitio',
            name='URLfoto',
        ),
        migrations.AddField(
            model_name='foto',
            name='sitio',
            field=models.ForeignKey(to='sitios.Sitio'),
        ),
    ]
