# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0004_auto_20151128_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulacoes',
            old_name='Seguro',
            new_name='ValorSeguro',
        ),
    ]
