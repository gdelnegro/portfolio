# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-06 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20160906_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP1', null=True, verbose_name='MDL1')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP2', null=True, verbose_name='MDL2')),
                ('tag', models.CharField(help_text='TTP32', max_length=20, unique=True, verbose_name='MDL32')),
                ('value', models.TextField(help_text='TTP34', verbose_name='MDL34')),
                ('value_en', models.TextField(help_text='TTP34', null=True, verbose_name='MDL34')),
                ('value_pt_br', models.TextField(help_text='TTP34', null=True, verbose_name='MDL34')),
            ],
            options={
                'verbose_name': 'MTA14',
                'verbose_name_plural': 'MTP14',
            },
        ),
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_tag',
            field=models.CharField(blank=True, help_text='TTP42', max_length=20, null=True, verbose_name='MDL42'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_text',
            field=models.TextField(blank=True, help_text='TTP43', null=True, verbose_name='MDL43'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_text_en',
            field=models.TextField(blank=True, help_text='TTP43', null=True, verbose_name='MDL43'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='auxiliary_text_pt_br',
            field=models.TextField(blank=True, help_text='TTP43', null=True, verbose_name='MDL43'),
        ),
    ]
