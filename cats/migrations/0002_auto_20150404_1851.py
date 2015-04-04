# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='blurb',
            field=models.TextField(max_length=5000, default=''),
        ),
        migrations.AddField(
            model_name='cat',
            name='pict_url',
            field=models.CharField(max_length=500, default=''),
        ),
    ]
