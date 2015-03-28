# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waterplants', '0002_userplants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplants',
            name='plantType',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
