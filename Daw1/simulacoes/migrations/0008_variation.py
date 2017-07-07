# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0007_auto_20151128_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=120)),
                ('Valor', models.IntegerField()),
                ('ValorSeguro', models.IntegerField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('Inventory', models.IntegerField(null=True, blank=True)),
                ('Simulacoes', models.ForeignKey(to='simulacoes.Simulacoes')),
            ],
        ),
    ]
