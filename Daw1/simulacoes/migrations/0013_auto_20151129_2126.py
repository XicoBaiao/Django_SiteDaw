# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0012_auto_20151129_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimulationImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'simulacoes/')),
                ('Simulacoes', models.ForeignKey(to='simulacoes.Simulacoes')),
            ],
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='simulacoes',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
