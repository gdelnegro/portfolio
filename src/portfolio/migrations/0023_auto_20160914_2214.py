# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_auto_20160909_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_string',
            field=models.TextField(help_text='TTP46', verbose_name='MDL46'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.TextField(blank=True, help_text='TTP45', null=True, verbose_name='MDL45'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='images',
            field=models.ManyToManyField(blank=True, help_text='TTP21', to='portfolio.Image', verbose_name='MDL21'),
        ),
        migrations.AlterField(
            model_name='translationtype',
            name='name',
            field=models.TextField(help_text='TTP3', verbose_name='MDL3'),
        ),
        migrations.AlterField(
            model_name='translationtype',
            name='name_en',
            field=models.TextField(help_text='TTP3', null=True, verbose_name='MDL3'),
        ),
        migrations.AlterField(
            model_name='translationtype',
            name='name_pt_br',
            field=models.TextField(help_text='TTP3', null=True, verbose_name='MDL3'),
        ),
    ]