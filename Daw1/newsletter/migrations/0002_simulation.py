# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='simulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Categoria', models.CharField(default=b'Tipo de aparelho', max_length=25, choices=[(b'1', b'Smartphone'), (b'2', b'Tablet'), (b'3', b'Port\xc3\xa1til'), (b'4', b'Televisor'), (b'5', b'C\xc3\xa2mara Fotogr\xc3\xa1fica'), (b'6', b'Outros')])),
                ('Nome', models.CharField(max_length=120, null=True, blank=True)),
                ('Valor', models.CharField(default=b'Valor do aparelho', max_length=25, choices=[(b'2', b'200-400'), (b'1', b'0-200'), (b'4', b'600+'), (b'3', b'400-600')])),
            ],
        ),
    ]
