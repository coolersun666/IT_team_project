# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manicurer', '0018_auto_20180321_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manicurer.Picture'),
        ),
    ]
