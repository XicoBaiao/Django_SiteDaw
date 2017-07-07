# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0006_simulacoes_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulacoes',
            old_name='Active',
            new_name='active',
        ),
    ]
