# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waterplants', '0004_auto_20150328_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplants',
            name='nextWaterTime',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
