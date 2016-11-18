# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_remove_libro_portada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamos',
            old_name='usaurio',
            new_name='usuario',
        ),
        migrations.AddField(
            model_name='prestamos',
            name='comentario',
            field=models.CharField(max_length=30, default=-9),
            preserve_default=False,
        ),
    ]
