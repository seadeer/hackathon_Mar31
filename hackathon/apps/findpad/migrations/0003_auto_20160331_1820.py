# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('findpad', '0002_auto_20160331_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='status',
        ),
        migrations.AddField(
            model_name='listing',
            name='isAvailable',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 31, 18, 20, 26, 65000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='pets',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='washer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
