# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 22:14:47
from __future__ import unicode_literals

from django.db import migrations


def __load_data(**kwargs):
    apps = kwargs.pop('apps', None)
    translation_type = apps.get_model("portfolio", "TranslationType")
    if apps:
        model = apps.get_model("portfolio", "Translation")
        try:
            mdl = model.objects.get(tag=kwargs['tag'])
        except model.DoesNotExist:
            mdl = model()
        except Exception as err:
            raise err
        for k, v in kwargs.items():
            if k == "type":
                setattr(mdl, k, translation_type.objects.get(tag=v))
            else:
                setattr(mdl, k, v)
        setattr(mdl, "migration_created", True)
        mdl.save()


def clear_data(apps, schema_editor):
    model = apps.get_model("portfolio", "Translation")
    model.objects.filter(tag__in=["MDL45","MDL46","MDL47"]).delete()


def load_data(apps, schema_editor):
    __load_data(apps=apps, tag="MDL45", type="MDL", text_pt_br="Título", text_en="Title", auxiliary_tag="TTP45", auxiliary_text_pt_br="Título da imagem", auxiliary_text_en="Image title")
    __load_data(apps=apps, tag="MDL46", type="MDL", text_pt_br="String binária", text_en="Image string", auxiliary_tag="TTP46", auxiliary_text_pt_br="String binária da imagem", auxiliary_text_en="Image binary string")
    __load_data(apps=apps, tag="MDL47", type="MDL", text_pt_br="Visualização da imagem", text_en="Image preview", auxiliary_tag="TTP47", auxiliary_text_pt_br="Visualização da imagem salva", auxiliary_text_en="Uploaded image preview")


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_auto_20160914_2214'),
    ]

    operations = [
        migrations.RunPython(load_data, clear_data)
    ]

        