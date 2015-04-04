# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('fluffy', models.BooleanField()),
                ('pettable', models.BooleanField()),
                ('adopted', models.BooleanField(default=False)),
                ('color', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
