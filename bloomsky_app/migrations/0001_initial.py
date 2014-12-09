# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceId', models.CharField(max_length=40)),
                ('sc', models.CharField(max_length=100)),
                ('sv', models.CharField(max_length=100)),
                ('firmwareVer', models.CharField(max_length=100)),
                ('hardwareVer', models.CharField(max_length=100)),
                ('productType', models.CharField(max_length=20)),
                ('productModel', models.CharField(max_length=20)),
                ('queueNum', models.PositiveIntegerField()),
                ('tS', models.PositiveIntegerField()),
                ('enR', models.CharField(max_length=40)),
                ('isOffline', models.PositiveSmallIntegerField()),
                ('isAtNight', models.SmallIntegerField()),
                ('lowVoltage', models.PositiveSmallIntegerField()),
                ('voltage', models.PositiveSmallIntegerField()),
                ('temperature', models.PositiveIntegerField()),
                ('humidity', models.PositiveSmallIntegerField()),
                ('uv', models.PositiveSmallIntegerField()),
                ('aPData_ts', models.PositiveIntegerField()),
                ('searialnum', models.PositiveSmallIntegerField()),
                ('photosensitive', models.PositiveSmallIntegerField()),
                ('outAtmosphericPressure', models.PositiveIntegerField()),
                ('rainfall', models.SmallIntegerField()),
                ('voltageStatus', models.SmallIntegerField()),
                ('poweradapterStatus', models.SmallIntegerField()),
                ('oVErr', models.SmallIntegerField()),
                ('powerOnTime', models.PositiveIntegerField()),
                ('wlanTime', models.PositiveIntegerField()),
                ('dHCPTime', models.PositiveIntegerField()),
                ('uploadTime', models.PositiveIntegerField()),
                ('device_ts', models.PositiveIntegerField()),
                ('isCharging', models.SmallIntegerField()),
                ('isEffective', models.PositiveIntegerField()),
                ('picture', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
