# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-06 13:08:58
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
    model.objects.filter(tag__in=["MDL40","MDL39","MDL41","GEN28"]).delete()


def load_data(apps, schema_editor):
    __load_data(apps=apps, tag="MDL40", type="MDL", text_pt_br="Gráfico em círculo", text_en="Gauge chart", auxiliary_tag="TTP40", auxiliary_text_pt_br="Gráfico em círculo", auxiliary_text_en="Gauge chart")
    __load_data(apps=apps, tag="MDL39", type="MDL", text_pt_br="Gráfico de barra de progresso", text_en="Progress bar chart", auxiliary_tag="TTP39", auxiliary_text_pt_br="Progress bar chart", auxiliary_text_en="Progress bar chart")
    __load_data(apps=apps, tag="MDL41", type="MDL", text_pt_br="Tipo de gráfico", text_en="Chart type", auxiliary_tag="TTP41", auxiliary_text_pt_br="O tipo de gráfico que será utilizado para representar essa habilidade", auxiliary_text_en="The chart type that will be used to represent this skill")
    __load_data(apps=apps, tag="GEN28", type="GEN", text_pt_br="Mais habilidades", text_en="More skills", auxiliary_tag="", auxiliary_text_pt_br="", auxiliary_text_en="")


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20160906_1300'),
    ]

    operations = [
        migrations.RunPython(load_data, clear_data)
    ]

        