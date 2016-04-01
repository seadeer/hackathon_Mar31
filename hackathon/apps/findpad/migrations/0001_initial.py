# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('isAvailable', models.BooleanField(default=True)),
                ('pets', models.BooleanField(default=False)),
                ('washer', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2016, 4, 1, 12, 30, 16, 525000))),
                ('lister', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'listings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=140)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2016, 4, 1, 12, 30, 16, 526000))),
                ('recipient', models.ForeignKey(to='findpad.Listing')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'messages',
            },
            bases=(models.Model,),
        ),
    ]
