# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-02 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecbyapi', '0014_housespec_reserrmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housespec',
            name='calc_done',
            field=models.BooleanField(default=False, verbose_name='一次エネルギー消費量計算済み'),
        ),
        migrations.AlterField(
            model_name='housespec',
            name='resErrMessage',
            field=models.CharField(blank=True, default='None', max_length=255),
        ),
    ]
