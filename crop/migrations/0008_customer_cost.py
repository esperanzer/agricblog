# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-01 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0007_auto_20190102_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cost',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]