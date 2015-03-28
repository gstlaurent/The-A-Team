# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waterplants', '0003_auto_20150328_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='interval',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userplants',
            name='nextWaterTime',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userplants',
            name='plantType',
            field=models.ForeignKey(to='waterplants.Plant'),
            preserve_default=True,
        ),
    ]
