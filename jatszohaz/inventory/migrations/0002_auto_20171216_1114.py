# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-16 11:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamepiece',
            name='game_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_pieces', to='inventory.GameGroup'),
        ),
        migrations.AddField(
            model_name='gamepiece',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='gamepack',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamepack',
            name='games',
            field=models.ManyToManyField(related_name='packs', to='inventory.GameGroup'),
        ),
    ]
