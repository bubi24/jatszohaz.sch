# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-12 06:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20171216_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamepack',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='gamepack',
            name='games',
        ),
        migrations.DeleteModel(
            name='GamePack',
        ),
    ]