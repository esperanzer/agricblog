# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-03 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0004_customer_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='other_details',
            field=models.TextField(blank=True, null=True, verbose_name='Other Details'),
        ),
    ]
