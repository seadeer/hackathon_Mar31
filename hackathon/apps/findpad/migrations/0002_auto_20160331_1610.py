# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('findpad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 31, 16, 10, 6, 831000)),
            preserve_default=True,
        ),
    ]
