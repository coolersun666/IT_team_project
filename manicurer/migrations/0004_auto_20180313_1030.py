# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manicurer', '0003_auto_20180313_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='avgrate',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='picture',
            name='owner',
            field=models.CharField(max_length=100),
        ),
    ]
