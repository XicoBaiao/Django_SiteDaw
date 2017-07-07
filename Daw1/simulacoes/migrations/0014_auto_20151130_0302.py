# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import simulacoes.models


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0013_auto_20151129_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulationimage',
            name='image',
            field=models.FileField(upload_to=simulacoes.models.image_upload_to),
        ),
    ]
