# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulacoes',
            name='ValorSeguro',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]
