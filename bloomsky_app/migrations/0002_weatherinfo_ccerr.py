# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloomsky_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherinfo',
            name='cCErr',
            field=models.SmallIntegerField(default='0'),
            preserve_default=False,
        ),
    ]
