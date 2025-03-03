# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jihanki', '0005_auto_20180125_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='loading',
            name='earnings',
            field=models.IntegerField(default=0, null=True, verbose_name='売上'),
        ),
        migrations.AddField(
            model_name='loading',
            name='xy',
            field=models.CharField(max_length=10, null=True, verbose_name='補充位置'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='jan_code_L',
            field=models.CharField(max_length=255, null=True, verbose_name='左JANコード'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='jan_code_R',
            field=models.CharField(max_length=255, null=True, verbose_name='右JANコード'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='stock_L',
            field=models.IntegerField(default=0, null=True, verbose_name='左在庫'),
        ),
        migrations.AlterField(
            model_name='earnings',
            name='stock_R',
            field=models.IntegerField(default=0, null=True, verbose_name='右在庫'),
        ),
    ]
