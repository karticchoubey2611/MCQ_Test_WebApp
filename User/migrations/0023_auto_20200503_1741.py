# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-05-03 17:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0022_auto_20200503_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstest',
            name='completion_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 20, 41, 49, 970394)),
        ),
    ]
