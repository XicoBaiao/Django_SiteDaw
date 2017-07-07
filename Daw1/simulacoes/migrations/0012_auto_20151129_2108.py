# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacoes', '0011_auto_20151128_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Image', models.FileField(upload_to=b'simulacoes/')),
                ('simulacoes', models.ForeignKey(to='simulacoes.Simulacoes')),
            ],
        ),
        migrations.RemoveField(
            model_name='variation',
            name='Inventory',
        ),
    ]
