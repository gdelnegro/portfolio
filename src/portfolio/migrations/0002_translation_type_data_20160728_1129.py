# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 11:29
from __future__ import unicode_literals

from django.db import migrations


def load_data(apps, schema_editor):
    translation = apps.get_model("portfolio", "TranslationType")
    translation(tag='MDL', name_pt_br="Modelo", name_en="Model", has_auxiliary_text=True, auxiliary_tag="TTP").save()
    translation(tag='MTA', name_pt_br="Meta", name_en="Meta", has_auxiliary_text=True, auxiliary_tag="MTP").save()
    translation(tag='GEN', name_pt_br="Texto", name_en="General Text", has_auxiliary_text="", auxiliary_tag="GTP").save()
    translation(tag='ME', name_pt_br="Mensagem de erro", name_en="Error message", has_auxiliary_text="",
                auxiliary_tag="MEE").save()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
