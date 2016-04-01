# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0002_auto_20160401_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 15, 54, 33, 688000, tzinfo=utc), verbose_name=datetime.datetime(2016, 4, 1, 8, 54, 19, 279000)),
            preserve_default=False,
        ),
    ]
