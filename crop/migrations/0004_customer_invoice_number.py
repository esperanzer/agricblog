# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-03 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]