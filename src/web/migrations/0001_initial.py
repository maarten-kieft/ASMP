# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-05 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'Meter',
            },
        ),
        migrations.CreateModel(
            name='MeterMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('usage_current', models.DecimalField(decimal_places=3, max_digits=10)),
                ('usage_total_low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('usage_total_normal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('return_current', models.DecimalField(decimal_places=3, max_digits=10)),
                ('return_total_low', models.DecimalField(decimal_places=3, max_digits=10)),
                ('return_total_normal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Meter')),
            ],
            options={
                'db_table': 'MeterMeasurement',
            },
        ),
    ]
