# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0010_auto_20151128_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='Nome',
            field=models.CharField(max_length=120),
        ),
    ]
