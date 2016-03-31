# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('bedrooms', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('status', models.BooleanField()),
                ('pets', models.BooleanField()),
                ('washer', models.BooleanField()),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 31, 16, 9, 37, 258000))),
                ('lister', models.ForeignKey(to='logreg.User')),
            ],
            options={
                'db_table': 'listings',
            },
            bases=(models.Model,),
        ),
    ]
