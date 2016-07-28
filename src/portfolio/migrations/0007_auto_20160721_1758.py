# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20160716_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('tag', models.CharField(help_text='TTP032', max_length=20, unique=True, verbose_name='MDL032')),
                ('value', models.TextField(help_text='TTP034', verbose_name='MDL034')),
            ],
            options={
                'verbose_name': 'MTA022',
                'verbose_name_plural': 'MTA023',
            },
        ),
        migrations.AlterField(
            model_name='translation',
            name='tag',
            field=models.CharField(help_text='TTP032', max_length=20, unique=True, verbose_name='MDL032'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='type',
            field=models.CharField(choices=[('MDL', 'MDL036'), ('TTP', 'MDL035'), ('MTA', 'MDL037'), ('MTP', 'MDL038'), ('GEN', 'MDL039'), ('GTP', 'MDL040')], help_text='TTP033', max_length=20, verbose_name='MDL033'),
        ),
    ]
