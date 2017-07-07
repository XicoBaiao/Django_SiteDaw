# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0002_simulacoes_valorseguro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulacoes',
            old_name='ValorSeguro',
            new_name='Seguro',
        ),
    ]
