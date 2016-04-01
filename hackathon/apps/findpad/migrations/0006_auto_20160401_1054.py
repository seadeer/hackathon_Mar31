# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0004_auto_20160401_1054'),
        ('findpad', '0005_auto_20160401_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=140)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2016, 4, 1, 10, 54, 27, 367000))),
                ('recipient', models.ForeignKey(to='findpad.Listing')),
                ('sender', models.ForeignKey(to='logreg.User')),
            ],
            options={
                'db_table': 'messages',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 4, 1, 10, 54, 27, 366000)),
            preserve_default=True,
        ),
    ]
