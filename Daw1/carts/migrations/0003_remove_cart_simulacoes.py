# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20151130_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Simulacoes',
        ),
    ]
