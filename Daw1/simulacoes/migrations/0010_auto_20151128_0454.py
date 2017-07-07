# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0009_auto_20151128_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='Nome',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AlterField(
            model_name='variation',
            name='Valor',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='ValorSeguro',
            field=models.IntegerField(),
        ),
    ]
