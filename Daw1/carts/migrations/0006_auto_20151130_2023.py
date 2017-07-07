# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20151130_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartsimulation',
            old_name='line_item_total',
            new_name='line_simulacoes_total',
        ),
    ]
