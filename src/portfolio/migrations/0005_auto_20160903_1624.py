# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-03 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20160903_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_tag',
            field=models.CharField(blank=True, help_text='TTP32', max_length=20, null=True, verbose_name='ToolTipTag'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_text',
            field=models.TextField(blank=True, help_text='TTP34', null=True, verbose_name='ToolTipText'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_text_en',
            field=models.TextField(blank=True, help_text='TTP34', null=True, verbose_name='ToolTipText'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_text_pt_br',
            field=models.TextField(blank=True, help_text='TTP34', null=True, verbose_name='ToolTipText'),
        ),
    ]