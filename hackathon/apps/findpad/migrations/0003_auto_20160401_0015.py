# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('findpad', '0002_auto_20160331_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 4, 1, 0, 15, 42, 75739)),
            preserve_default=True,
        ),
    ]
