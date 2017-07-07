# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0003_auto_20151128_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacoes',
            name='Seguro',
            field=models.IntegerField(default=b''),
        ),
    ]
