# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-18 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0011_auto_20160918_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='value',
            field=models.PositiveSmallIntegerField(help_text='1 is the worst, 4 is the best'),
        ),
    ]
