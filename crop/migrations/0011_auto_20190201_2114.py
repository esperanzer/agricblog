# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-01 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0010_auto_20190201_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expiry_date',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufactured',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
    ]