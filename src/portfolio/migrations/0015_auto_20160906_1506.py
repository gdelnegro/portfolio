# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-06 15:06:16
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
    model.objects.filter(tag__in=["GEN31","GEN30"]).delete()


def load_data(apps, schema_editor):
    __load_data(apps=apps, tag="GEN31", type="GEN", text_pt_br="Uma oportunidade de trabalhar, aprender e me aprimorar, assim como fazer parte de uma organização (ou projeto) que tenha como objetivos aprimorar o mercado e entregar e melhorar a experiência do usuário.", text_en="An opportunity to work, learn and improve myself, as well as being involved in an organization (or project) that aims to improve the user experience and improve the market.", auxiliary_tag="", auxiliary_text_pt_br="", auxiliary_text_en="")
    __load_data(apps=apps, tag="GEN30", type="GEN", text_pt_br="Sou um desenvolvedor Full Stack, focado em resolução de problemas e melhorar a experiência do usuário, com experiência em desenvolvimento web e manutenção/melhorias em infraestrutura (em nuvem ou física) . Tenho experiência com Python, PHP, além de JavaScript, Jquery, AngularJS, MySQL, PostgreSQL, DynamoDB e Aerospike.
Sinta-se a vontade, para me mandar uma mensagem.", text_en="I'm a Full Stack developer, focused in problem solving and improving the user experience, with experience in web development and infrastructure (cloud or bare metal) maintenance/upgrade. I have experience with Python and PHP, JavaScript, jQuery, AngularJs, along with MySQL, PostgreSQL, DynamoDB and Aerospike.
Feel free to have a chat with me.", auxiliary_tag="", auxiliary_text_pt_br="", auxiliary_text_en="")


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20160906_1454'),
    ]

    operations = [
        migrations.RunPython(load_data, clear_data)
    ]

        