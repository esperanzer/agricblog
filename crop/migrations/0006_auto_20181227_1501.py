# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-27 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0005_auto_20181203_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='address',
        ),
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phone',
        ),
    ]