# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-16 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('tag', models.CharField(help_text='TTP032', max_length=20, verbose_name='MDL032')),
                ('type', models.CharField(choices=[('MDL', 'MDL036'), ('TTP', 'MDL035'), ('MTA', 'MDL037'), ('MTP', 'MDL038')], help_text='TTP033', max_length=20, verbose_name='MDL033')),
                ('text', models.TextField(help_text='TTP034', verbose_name='MDL034')),
            ],
            options={
                'verbose_name': 'MTA020',
                'verbose_name_plural': 'MTA021',
            },
        ),
    ]