# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-09-18 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0012_auto_20160919_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='proposal',
            new_name='ranking',
        ),
    ]