# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20151130_0317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Simulacoes',
            new_name='simulacoes',
        ),
        migrations.RenameField(
            model_name='cartsimulation',
            old_name='Simulacoes',
            new_name='simulacoes',
        ),
        migrations.AddField(
            model_name='cartsimulation',
            name='line_item_total',
            field=models.IntegerField(default=19.99),
            preserve_default=False,
        ),
    ]
