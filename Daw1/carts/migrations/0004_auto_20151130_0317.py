# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0014_auto_20151130_0302'),
        ('carts', '0003_remove_cart_simulacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Simulacoes',
            field=models.ManyToManyField(to='simulacoes.Variation', through='carts.CartSimulation'),
        ),
        migrations.AddField(
            model_name='cartsimulation',
            name='cart',
            field=models.ForeignKey(default=1, to='carts.Cart'),
            preserve_default=False,
        ),
    ]
