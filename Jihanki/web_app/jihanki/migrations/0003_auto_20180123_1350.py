# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jihanki', '0002_auto_20180123_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='gen',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=30, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='pro',
            field=models.CharField(choices=[('公務員', '公務員'), ('経営者・役員', '経営者・役員'), ('会社員', '会社員'), ('自営業', '自営業'), ('専業主婦', '専業主婦'), ('パート・アルバイト', 'パート・アルバイト'), ('学生', '学生'), ('その他', 'その他')], max_length=30, verbose_name='職業'),
        ),
    ]
