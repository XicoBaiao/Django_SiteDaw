# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0008_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='Nome',
            new_name='Seguro',
        ),
    ]
