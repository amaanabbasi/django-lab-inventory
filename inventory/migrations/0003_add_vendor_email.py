# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-09 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20170623_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='rep_email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='rep_email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]