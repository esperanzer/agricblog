# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-26 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_auto_20181126_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
