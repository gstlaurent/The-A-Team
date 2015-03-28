# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waterplants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlants',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nextWaterTime', models.TimeField()),
                ('plantType', models.ForeignKey(to='waterplants.Plant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
