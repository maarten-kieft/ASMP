# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-17 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_setting'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='LogMessage',
        ),
        migrations.AlterModelTable(
            name='logmessage',
            table='LogMessage',
        ),
    ]
