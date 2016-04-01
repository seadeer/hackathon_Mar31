# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('findpad', '0004_auto_20160401_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 4, 1, 8, 54, 19, 280000)),
            preserve_default=True,
        ),
    ]
